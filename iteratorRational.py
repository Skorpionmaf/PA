import random


class Rational():

    def __init__(self, num, den):
        if num == den:
            den = num = 1
        self.setNum(num)
        self.setDen(den)

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den

    def setNum(self, num):
        self.__num = num

    def setDen(self, den):
        if den == 0:
            raise ValueError("Divisione per zero")
        else:
            self.__den = den

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.getNum() == other.getNum() and self.getDen() == other.getDen()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str(self.__num)+"/"+str(self.__den)

    def __hash__(self):
        return hash((self.__num, self.__den))

    num = property(getNum, setNum)
    den = property(getDen, setDen)


class RandomRational():

    def __init__(self, minvalue, maxvalue, seedvalue, maxrandomvalue):
        self.__min = minvalue
        self.__max = maxvalue
        self.__seed = seedvalue
        self.__maxrandomvalue = maxrandomvalue

    def __iter__(self):
        random.seed(self.__seed)
        self.__count = 0
        return self

    def __next__(self):
        if self.__count <= self.__maxrandomvalue:
            self.__count += 1
            randomIntegerNum = random.randint(self.__min, self.__max)
            randomIntegerDen = random.randint(self.__min, self.__max)
            return Rational(randomIntegerNum, randomIntegerDen)
        else:
            raise StopIteration

if __name__ == '__main__':
    iteratorRational = RandomRational(1, 100, 1)
    for i in range(0, 100):
        RationalTemp = next(iteratorRational)
        print(RationalTemp)

    print(Rational(1, 0))
    Rat1 = Rational(5, 6)
    Rat1.den = 0
    print(Rat1)