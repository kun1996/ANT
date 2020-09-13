import operator


class Node:

    def __init__(self, atom, next_node):
        self.atom = atom
        self.next_node = next_node

    def run(self, ctx):
        c = self.atom.exec(ctx)
        ctx.update(c)

        self.next_node.run(ctx)


class StartNode(Node):

    def run(self, ctx):
        self.next_node.run(ctx)


class StopNode(Node):

    def run(self, ctx):
        pass


class IfNode(Node):
    OPERATOR_DICT = {
        '<': operator.lt,
        '<=': operator.le,
        '=': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '>': operator.gt,
    }
    COMPARE_KEY = 'num_return'

    def __init__(self, atom, operator_list):
        """
        :param atom:
        :param operator_list: [(op, v, node)]
        """
        super().__init__(atom, None)
        self.operator_list = operator_list

    def run(self, ctx):
        c = self.atom.exec(ctx)
        ctx.update(c)

        compare_value = ctx.get(self.COMPARE_KEY, '')

        for op, v, node in self.operator_list:
            if self.OPERATOR_DICT[op](compare_value, v):
                ctx.pop(self.COMPARE_KEY)  # 取消条件判断的上下文
                return node.run(ctx)

        raise Exception('if node not match True result, please check it!!!')
