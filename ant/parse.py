import re
from collections import defaultdict

RULE_FLAG = 0

RULE_PREFIX = '>>>'
RULE_KEY = '[a-zA-Z_]\\w*?'
RULE_SEQ = ':'
RULE_VALUE = '(?:.|\n)*?'
RULE_SUFFIX = '<<<'

# RULE = f'{RULE_PREFIX}({RULE_KEY}){RULE_SEQ}({RULE_VALUE})?{RULE_SUFFIX}'
RULE = '%s(%s)%s(%s)%s' % (RULE_PREFIX, RULE_KEY, RULE_SEQ, RULE_VALUE, RULE_SUFFIX)

RUKE_KEY_HOOK_DICT = {
    # 'ips': lambda v: print(v),
}


class Parse:

    def __init__(self, s):
        if isinstance(s, bytes):
            s = str(s, encoding='utf-8', errors='ignore')
        self.s = s

    def parse(self, data=None):
        data = data or defaultdict(list)

        for k, v in re.findall(RULE, self.s, RULE_FLAG):
            if k in RUKE_KEY_HOOK_DICT:
                RUKE_KEY_HOOK_DICT[k](v)

            data[k].append(v)
        return data
