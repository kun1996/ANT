class DummyFile:

    def __init__(self, s):
        self.s = s
        self._index = 0

    def read(self, size=None):
        size = size or -1
        if size < 0:
            return self.s

        s = self.s[self._index: self._index + size]
        self._index += size

        return s

    def close(self):
        pass
