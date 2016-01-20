import functools

def filter_cars(x):
    l = list(x)
    cars = [';', ':', '.', ',', '\"', '\'', '[', ']', '{', '}', '(', ')']
    l_new = list(map(lambda x: " " if x in cars else x, l))
    return "".join(l_new).split()

class UpDownFile:
    def __init__(self, path_file):
        self.path = path_file

    def __iter__(self):
        self.fr = open(self.path, "r")
        self.cache = []
        self.index = 0

        return self

    def __next__(self):
        if self.index == len( self.cache ):
            new_words = self.fr.read(256).split()
            new_words = list( map(filter_cars, new_words) )

            if len(new_words) == 0:
                raise StopIteration
            else:
                new_words = functools.reduce(lambda x, y: x+y, new_words)
                for x in new_words: self.cache.append(x)

        res = self.cache[self.index]
        self.index += 1
        
        return res

    def ungetw(self):
        self.index -= 1