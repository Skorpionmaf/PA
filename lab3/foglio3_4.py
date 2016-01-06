
class MyDict:

    def __init__(self, d):
        self.md = d
        keys = sorted(self.md.keys())

        self.order = dict()
        i = 0
        for k in keys:
            self.order[i] = k
            i += 1

        self.nextk = i

    def add(self, key, value):
        self.md[key] = value
        keys = sorted(self.md.keys())

        self.order = dict()
        i = 0
        for k in keys:
            self.order[i] = k
            i += 1

        self.nextk = i

    def take(self, key):
        return self.md[key]

    def disp(self):
        s = "dict: { "
        for i in self.order.keys():
            x = self.order[i]
            y = self.md[ self.order[i] ]

            if (type(x) == str):
                px = '\'' + str(x) + '\''
            else:
                px = str(x)
            if (type(y) == str):
                py = '\'' + str(y) + '\''
            else:
                py = str(y)

            if i > 0:

                s += ', ' + px + ': ' + py
            else:
                s += px + ': ' + py
        s += " } "

        return s