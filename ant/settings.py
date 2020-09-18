import os
import stat

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

FLOW_SERVER_NAME = 'flow'
CTX_SEQ = ','

FILE_PERMISSION = stat.S_IRUSR | stat.S_IXUSR
TEMP_DIR = '/tmp/__ant__%s'

TIMEOUT = 30


HOST_DICT = {
    'HOST1': {
        'hostname': '192.168.52.201',
        'username': 'root',
        'password': '123456',
        'pkey': None,  # 私钥文件路径
        'timeout': 10,
    },
}

SERVER_DICT = {
    'BASE': {
        'file': os.path.join(BASE_DIR, 'test/test.sh'),
        'user': 'root',
        'group': 'root',
        'timeout': 30,
        'context': {
            'a': 'aaaaa',
            'c': 'aaaaa',
        },
        'server': [HOST_DICT['HOST1']],
    },
    'BASE2': {
        'file': os.path.join(BASE_DIR, 'test/test.sh'),
        'user': 'root',
        'group': 'root',
        'timeout': 30,
        'context': {
            'b': 'bbbbbb'
        },
        'server': [HOST_DICT['HOST1']],
    },
    'IF': {
        'file': os.path.join(BASE_DIR, 'test/test_if.sh'),
        'user': 'root',
        'group': 'root',
        'timeout': 30,
        'context': {
            'bool': 'if',
        },
        'server': [HOST_DICT['HOST1']],
    },
    'IF_TRUE': {
        'file': os.path.join(BASE_DIR, 'test/test_if_true.sh'),
        'user': 'root',
        'group': 'root',
        'timeout': 30,
        'context': {
            'bool': 'true',
        },
        'server': FLOW_SERVER_NAME,
    },
    'IF_FALSE': {
        'file': os.path.join(BASE_DIR, 'test/test_if_false.sh'),
        'user': 'root',
        'group': 'root',
        'timeout': 30,
        'context': {
            'bool': 'false',
        },
        'server': [HOST_DICT['HOST1']],
    }
}
