import os
import sys
import secrets
import copy
from typing import Dict
import select

import paramiko

from .settings import SERVER_DICT, FLOW_SERVER_NAME, CTX_SEQ, TIMEOUT, TEMP_DIR, FILE_PERMISSION
from .file import DummyFile
from .parse import Parse
from .server import FlowServer


class Client:
    SSH_CLIENT = paramiko.SSHClient
    SFTP_CLIENT = paramiko.SFTPClient
    POLICY = paramiko.AutoAddPolicy

    TEMP_DIR = TEMP_DIR
    TIMEOUT = TIMEOUT
    FILE_PERMISSION = FILE_PERMISSION

    def __init__(self, server: str, context: Dict[str, str] = None):
        self.cfg = copy.deepcopy(SERVER_DICT[server])

        self.ctx = context or {}
        self._f_ctx = {}
        self.temp_dir = self.TEMP_DIR % secrets.token_hex(16)

    def _upload_file(self, sftp, path, remotepath):
        with open(path) as f:
            return sftp.putfo(DummyFile(f.read()), remotepath)

    def _upload_str_or_byte(self, sftp, s, remotepath):
        return sftp.putfo(DummyFile(s), remotepath)

    def _upload(self, sftp, path, remotepath, file=True):
        if file:
            return self._upload_file(sftp, path, remotepath)

        return self._upload_str_or_byte(sftp, path, remotepath)

    def _change_mod(self, sftp, remotepath, mod=None):
        mod = mod or self.FILE_PERMISSION
        sftp.chmod(remotepath, mod)

    def _set_env(self):
        fc = copy.deepcopy(self._f_ctx)
        c = copy.deepcopy(self.cfg.get('context', {}))
        c.update(self.ctx)
        fc.update(c)
        return '\n'.join([f"export {k}='{v}'" for k, v in fc.items()])

    def _eval_shell(self, path):
        return path

    def _shell(self, path):
        s = [
            f'#!/bin/bash',
            self._set_env(),  # 设置环境变量
            self._eval_shell(path),  # 执行脚本
        ]
        return '\n'.join(s)

    def exec_one(self, server, data):
        policy = self.POLICY
        ssh_client = self.SSH_CLIENT()
        ssh_client.set_missing_host_key_policy(policy())

        # 创建链接
        ssh_client.connect(**server)
        transport = ssh_client.get_transport()
        sftp_client = self.SFTP_CLIENT.from_transport(transport)

        # 创建临时目录
        stdin, stdout, stderr = ssh_client.exec_command(f'mkdir -p {self.temp_dir}')
        err_msg = stderr.read()
        if len(err_msg) > 0:
            raise Exception(err_msg)

        # 创建环境变量

        # 上传脚本
        remote_path = os.path.join(self.temp_dir, secrets.token_hex(16)).replace('\\', '/')
        remote_eval_path = os.path.join(self.temp_dir, secrets.token_hex(16)).replace('\\', '/')
        self._upload(
            sftp_client,
            self._shell(remote_eval_path),
            remote_path,
            file=False
        )
        self._change_mod(sftp_client, remote_path)

        self._upload(
            sftp_client,
            self.cfg.get('file'),
            remote_eval_path,
            file=True
        )
        self._change_mod(sftp_client, remote_eval_path)

        # 执行脚本
        timeout = self.cfg.get('timeout') or self.TIMEOUT
        chan = ssh_client._transport.open_session(timeout=timeout)
        chan.set_combine_stderr(True)
        chan.settimeout(timeout)
        u = self.cfg.get("user")
        g = self.cfg.get("group") or u
        chan.exec_command(
            f'chown -R {u}:{g} {self.temp_dir};\nsu - {u} -c {remote_path}'
        )
        msg, exit_code = self._recv_data(chan.makefile("r"), timeout, want_exitcode=True)

        # 执行完毕，删除目录
        ssh_client.exec_command(
            f'rm {"%s %s" % (remote_path,remote_eval_path)} && rmdir {self.temp_dir}'
        )

        # 关闭
        sftp_client.close()
        ssh_client.close()

        if exit_code != 0:
            raise Exception('Atom execute failed ...')

        data = Parse(msg).parse(data=data)
        return data

    def _recv_data(self, stdout, timeout, want_exitcode=False):
        channel = stdout.channel

        # read stdout/stderr in order to prevent read block hangs
        stdout_chunks = [channel.recv(len(channel.in_buffer))]
        # chunked read to prevent stalls
        while not channel.closed or channel.recv_ready():
            # stop if channel was closed prematurely, and there is no data in the buffers.
            got_chunk = False
            readq, _, _ = select.select([channel], [], [], timeout)
            for c in readq:
                if c.recv_ready():
                    stdout_chunks.append(channel.recv(len(c.in_buffer)))
                    sys.stdout.write(str(stdout_chunks[-1], encoding='utf-8', errors='ignore'))
                    got_chunk = True
            '''
            1) make sure that there are at least 2 cycles with no data in the input buffers in order to not exit too early (i.e. cat on a >200k file).
            2) if no data arrived in the last loop, check if we already received the exit code
            3) check if input buffers are empty
            4) exit the loop
            '''
            if not got_chunk and channel.exit_status_ready() and not channel.recv_ready():
                # indicate that we're not going to read from this channel anymore
                channel.shutdown_read()
                # close the channel
                channel.close()
                break  # exit as remote side is finished and our bufferes are empty

        # close all the pseudofiles
        stdout.close()

        if want_exitcode:
            # exit code is always ready at this point
            return b''.join(stdout_chunks), channel.recv_exit_status()
        return b''.join(stdout_chunks)

    def exec(self, f_ctx=None):
        self._f_ctx = f_ctx or {}

        server_list = self.cfg.get('server')
        if server_list == FLOW_SERVER_NAME:
            server_list = FlowServer().server(f_ctx)
        else:
            server_list = FlowServer().server(f_ctx, other_kw=server_list)

        data = None
        for server in server_list:
            data = self.exec_one(server, data)

        return {k: CTX_SEQ.join(v) for k, v in data.items()}
