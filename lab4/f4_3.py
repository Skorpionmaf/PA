
class Pascal:

    def __init__(self, m):
        self.max = m

    def __iter__(self):
        self.i = 0
        self.a = [1]

        return self

    def __next__(self):
        res = self.a

        self.b = [1]
        j = 0
        while j < self.i:
            self.b.append( self.a[j] + self.a[j+1] )
            j += 1

        self.b.append(1)
        self.i += 1
        self.a = self.b

        if self.i > self.max:
            raise StopIteration

        return res

