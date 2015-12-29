import operator

class PolishCalculator:

    def __init__(self):
        self._operand = { '+': operator.add, '-': operator.sub, '*': operator.mul, '**': operator.pow, 'or': operator.or_, 'not': operator.not_, 'and': operator.and_ }
        self._stack = []
        self._infix = []
        self._regular = ""

    def eval(self, string):
        l = string.split(sep = ' ')

        self._expr = []
        t = ['True', 'T', 't', 'TRUE']
        f = ['False', 'F', 'f', 'FALSE']
        for el in l:
            if el.isdigit() or (el in self._operand.keys()) or (el in t) or (el in f):
                if el.isdigit():
                    new = float(el)
                elif el in t:
                    new = True
                elif el in f:
                    new = False
                else:
                    new = el

                self._expr.append(new)

        for x in self._expr:
            if type(x) == float:
                self._stack.append(x)
                self._infix.append(str(x))

            elif type(x) == bool:
                self._stack.append(x)
                self._infix.append(str(x))

            elif (x in self._operand.keys()):
                b = self._stack.pop()
                a = self._stack.pop()
                B = self._infix.pop()
                A = self._infix.pop()

                self._infix.append( '(' + A +' ' + x + ' ' + B + ')' )
                self._stack.append( self._operand[x](a, b) )

            print( self._stack[-1] )
            print( self._infix[-1] )

        self._regular = self._infix.pop()
        self.result = self._stack.pop()

        return  self.result

    def __str__(self):
        if self._regular == "":
            return "Non è ancora stata valutata nessuna espressione"
        else:
            return self._regular
