from .settings import HOST_DICT, CTX_SEQ
from .parse import FLOW_IPS


class Server:
    def server(self):
        raise ImportError('Server need overwrite server method')


class IpServer(Server):
    def __init__(self, host_list):
        self.host_list = host_list

    def server(self):
        return self.host_list


class FlowServer(Server):

    def server(self, ctx):
        ips = ctx.get(FLOW_IPS, '').split(CTX_SEQ)
        if not ips:
            raise Exception(f'{FLOW_IPS} is empty, please check it')

        # 去主机列表找到执行主机并返回
        host_list = []
        for _, host in HOST_DICT.items():
            if host.get('hostname') in ips:
                host_list.append(host)

        return host_list
