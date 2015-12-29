import functools
import operator

class PolishCalculator:

    def __init__(self):
        self._stack = []
        self._operand = { '+': operator.add, '-': operator.sub, '*': operator.mul, '**': operator.pow, 'or': operator.or_, 'not': operator.not_, 'and': operator.and_ }
        self.result = 0

    def eval(self, str):
        l = list(str)
        l.reverse()

        for el in l:
            if (el.isdigit() == True) or ((el in self._operand.keys()) == True):
                if (el.isdigit() == True):
                    new = float(el)
                else:
                    new = el
                self._stack.append(new)

        while len(self._stack) > 0:
            buff = []
            x = self._stack.pop()

            while (x in self._operand.keys()) == False:
                buff.append(x)
                x = self._stack.pop()

            tot = functools.reduce(self._operand[x], buff)
            self.result = self._operand[x](self.result, tot)

        return self.result

    def __str__(self):
        s = ""
        
        return s