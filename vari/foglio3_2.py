import itertools
import operator

class Monoid:
    _op = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '|': operator.or_, '&': operator.and_, \
            '%': operator.mod, 'composition': lambda a, b: ( lambda x: a(b(x)) ),  }

    def __init__(self, set, operation, i, mod_card):

        self._operation = operation
        if mod_card:
            self._card = len(set)
        else:
            self._card = -1

        #check identity element
        for e in set:
            if i not in set:
                raise Exception('The identity element specified is not in the set!!')
            if self._ope(e, i) != e:
                raise Exception('The identity element passed to the class is not really an identity element for the set')

        #check associative and closure property
        for c in itertools.combinations(set, 3):
            if self._ope( self._ope(c[0], c[1]), c[2] ) != self._ope( c[0], self._ope(c[1], c[2]) ):
                raise Exception('The operation is not associative in the set given')
            if self._ope(c[0], c[1]) not in set:
                raise Exception('Closure property is violeted')

        self.set = set
        self.i = i

    def _ope(self, a, b):
        if self._card > 0:
            return ( self._op[self._operation](a, b) )%self._card
        else:
            return self._op[self._operation](a, b)

    def add(self, a, b, type = 'not boolean'):
        if a not in self.set or b not in self.set:
            raise Exception('The elements you want to add are not present in the set of the class')

        if type == 'boolean':
            return bool( self._ope(a, b) )
        else:
            return self._ope(a, b)

class Group(Monoid):

    def __init__(self, set, operation, i, mod_card):

        super().__init__(set, operation, i, mod_card)

        inv = []
        for g in set:
            for h in set:
                if self._ope(g, h) == i and self._ope(h, g) == i:
                    inv.append(h)

            if len(inv) == 0:
                raise Exception('Non esiste elemento inverso')

            inv.clear()



