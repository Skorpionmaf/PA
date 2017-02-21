class Mydict(dict):

    def __init__(self):
        super(Mydict, self).__init__()
        self.__orderedPairs = []

    def __setitem__(self, key, value):
        super(Mydict, self).__setitem__(key, value)
        self.__orderedPairs.append((key, value))
        self.__orderedPairs = sorted(self.__orderedPairs, key=lambda x: x[0])

    def items(self):
        return self.__orderedPairs

    def __str__(self):
        stringFormat = lambda x: "'"+str(x)+"'" if isinstance(x, str) else str(x)
        listStringx = list(map(stringFormat, [x for x, y in self.__orderedPairs]))
        listStringy = list(map(stringFormat, [y for x, y in self.__orderedPairs]))
        listString = zip(listStringx, listStringy)
        return "{" + ", ".join([x+": "+y for x, y in listString]) + "}"

if __name__ == '__main__':
    miodictOld = dict()
    miodict = Mydict()
    miodict["cavallo"] = 1
    miodict["cane"] = 2
    miodict["gatto"] = 3
    miodictOld["cavallo"] = 1
    miodictOld["cane"] = 2
    miodictOld["gatto"] = 3
    print(miodict)
    print(miodictOld)
    print(miodict.items())