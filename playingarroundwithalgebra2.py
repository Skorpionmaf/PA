from iteratorRational import *
from itertools import combinations


def genFunc(n):
    def func(a, b):
        return (a+b) % n
    return func


class NaturalIterator(object):

    def __init__(self, maxvalue):
        self.__max = maxvalue

    def __iter__(self):
        self.__num = 0
        return self

    def __next__(self):
        if self.__num <= self.__max:
            Num = self.__num
            self.__num += 1
            return Num
        else:
            raise StopIteration


class Ziterator(object):

    def __init__(self, minvalue, maxvalue, maxrandomvalue):
        self.__max = maxvalue
        self.__min = minvalue
        self.__maxrandomvalue = maxrandomvalue

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        if self.__count <= self.__maxrandomvalue:
            randint = random.randint(self.__min, self.__max)
            self.__count += 1
            return randint
        else:
            raise StopIteration


class Monoid(object):

    def __init__(self, mset, add, i):
        self.setMonoid(mset, add, i)

    def getMonoid(self):
        return (self.__set, self.__add, self.__i)

    def checkIdentity(mset, add, i):
        for elem in mset:
            if elem != add(elem, i):
                print(elem, add(elem, i), i)
                raise ValueError("checkIdentity Failed")

    def checkClosure(mset, add):
        couples = [(a, b) for a in mset for b in mset]
        for a, b in couples:
            if not isinstance(add(a, b), type(a)):
                raise ValueError("checkClosure Failed")

    def checkAssociativity(mset, add):
        triple = [(a, b, c) for a in mset for b in mset for c in mset]
        for a, b, c in triple:
            if add(add(a, b), c) != add(a, add(b, c)):
                raise ValueError("checkAssociativity Failed")

    def setMonoid(self, mset, add, i):
        Monoid.checkIdentity(mset, add, i)
        Monoid.checkAssociativity(mset, add)
        Monoid.checkClosure(mset, add)
        print("È un monoide")
        self.__set = mset
        self.__add = add
        self.__i = i


class Group(Monoid):

    def __init__(self, mset, add, i, invAdd):
        self.setGroup(mset, add, i, invAdd)

    def getGroup(self):
        return(self.__mset, self.__add, self.__i)

    def checkInvertibility(mset, invAdd, i):
        for elem in mset:
            if invAdd(elem) != i:
                return False
        return True

    def setGroup(self, mset, add, i, invAdd):
        Group.checkIdentity(mset, add, i)
        Group.checkAssociativity(mset, add)
        Group.checkClosure(mset, add)
        Group.checkInvertibility(mset, invAdd, i)
        print("È un gruppo")
        self.__set = mset
        self.__add = add
        self.__i = i


class Ring():

    def __init__(self, mset, add, i, invAdd, prod):
        self.setRing(mset, add, i, invAdd, prod)

    def getRing(self):
        return(self.__mset, self.__add, self.__i, self.__invAdd, self.__prod)

    def setRing(self, mset, add, i, invAdd, prod):
        self.__monoid = Monoid(mset, prod, i)
        Ring.checkCommutativity(mset, add)
        self.__group = Group(mset, add, i, invAdd)
        print("È un anello")
        self.__set = mset
        self.__add = add
        self.__i = i
        self.__invAdd = invAdd
        self.__prod = prod

    def checkCommutativity(mset, add):
        comb = combinations(mset, 2)
        for a, b in comb:
            if add(a, b) != add(b, a):
                raise ValueError("checkCommutativity Failed")