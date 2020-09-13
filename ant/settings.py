import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SERVER_DICT = {
    'BASE': {
        'file': os.path.join(BASE_DIR, 'test/test.sh'),
        'user': 'root',
        'group': 'root',
        'timeout': 30,
        'context': {
            'a': 'aaaaa'
        },
        'server': [{
            'hostname': '192.168.52.201',
            'username': 'root',
            'password': '123456',
            'pkey': None,  # 私钥文件路径
            'timeout': 10,
        }, {
            'hostname': '192.168.52.201',
            'username': 'root',
            'password': '123456',
            'pkey': None,  # 私钥文件路径
            'timeout': 10,
        }],
    },
    'BASE2': {
        'file': os.path.join(BASE_DIR, 'test/test.sh'),
        'user': 'root',
        'group': 'root',
        'timeout': 30,
        'context': {
            'b': 'bbbbbb'
        },
        'server': [{
            'hostname': '192.168.52.201',
            'username': 'root',
            'password': '123456',
            'pkey': None,  # 私钥文件路径
            'timeout': 10,
        }],
    }
}
