from .ssh import Client


class Flow:

    def __init__(self, node, ctx=None):
        self.node = node
        self.ctx = ctx or {}

    def run(self):
        self.node.run(self.ctx)
