from .ssh import Client


class Flow:

    def __init__(self, *args, ctx=None):
        self.atom_list = args
        self.ctx = ctx or {}

    def run(self):
        for atom in self.atom_list:
            c = Client(atom, self.ctx)
            self.ctx.update(c.exec())
