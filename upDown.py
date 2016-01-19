
class UpDownFile:

    def __init__(self, path_file):
        self.path = path_file

    def __iter__(self):
        self.fr = open(self.path, "r")
        self.content = self.fr.read().split()
        self.index = 0
        self.finish = len(self.content) -1

        return self

    def __next__(self):
        while self.index <= self.finish:
            res = self.content[self.index]
            self.index += 1
            return res

        if self.index > self.finish:
            self.fr.close()
            raise StopIteration

    def ungetw(self):
        self.index -= 1