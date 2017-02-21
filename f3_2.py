import itertools, random

class Monoid:
    def __init__(self, set, operation, i, infinite_set = False):

        self._ope = operation
        self._inf = infinite_set

        if not self._inf:
            #check identity element
            if i not in set:
                raise Exception('The identity element specified is not in the set!!')
            for e in set:
                if self._ope(i, e) != e:
                    raise Exception('The identity element passed to the class is not really an identity element for the set')
            #check associative and closure property
            for c in itertools.combinations_with_replacement(set, 3):
                res1 = self._ope( self._ope(c[0], c[1]), c[2] )
                res2 = self._ope( c[0], self._ope(c[1], c[2]) )

                if res1 not in set:
                    raise Exception('Closure property is violeted')

                    if res1 != res2:
                        raise Exception('The operation is not associative in the set given')
        else:
            #check identity element
            if not set.hasIn(i):
                raise Exception('The identity element specified is not in the set!!')
            for e in set.randomSample():
                if self._ope(i, e) != e:
                    raise Exception('The identity element passed to the class is not really an identity element for the set')

            #check associative and closure property
            for c in itertools.combinations_with_replacement(set.randomSample(), 3):
                res1 = self._ope( self._ope(c[0], c[1]), c[2] )
                res2 = self._ope( c[0], self._ope(c[1], c[2]) )

                if not set.hasIn(res1):
                    raise Exception('Closure property is violeted')

                    if res1 != res2:
                        raise Exception('The operation is not associative in the set given')

        self._set = set
        self._i = i

    def add(self, a, b, type = 'not boolean'):
        if a not in self._set or b not in self._set:
            raise Exception('The elements you want to add are not present in the set of the class')

        if type == 'boolean':
            return bool( self._ope(a, b) )
        else:
            return self._ope(a, b)

    def __str__(self):
        s = "Sono un Monoide con elementi:\n"
        for el in self._set: s += str(el) + '\n'

        s += "identity: {0} \n".format(self._i)
        return s

class Group(Monoid):
    def __init__(self, set, operation, i):

        super().__init__(set, operation, i)

        #check for invetibility
        inv = []
        for g in set:
            for h in set:
                if self._ope(g, h) == i and self._ope(h, g) == i:
                    inv.append(h)

            if len(inv) == 0:
                raise Exception('Non esiste elemento inverso')

            inv.clear()

    def __str__(self):
        s = "Sono un Gruppo con elementi:\n"
        for el in self._set: s += str(el) + '\n'

        s += "identity: {0} \n".format(self._i)
        return s

class IntegerSetFinite:
    # iterator that retun at each interationa a tuple of opposite integer like (-2, 2) while the positive one < max
    def __init__(self, min, max):
        self.max = max
        self.min = min

    def __iter__(self):
        self.curr = self.min
        return self

    def __next__(self):
        r = self.curr

        if self.curr > self.max:
            raise StopIteration

        self.curr += 1
        return r


class InfiniteIntegerSet:

    def __init__(self, notInSet):
        self.notInSet = notInSet
        self.min = -1000
        self.min = 1000

    def hasIn(self, element):

        if (type(element) == int) and (element not in self.notInSet):
            return True
        else:
            return False

    def randomSample(self):

        return random.sample(range(self.min, self.max), 100)

class InfiniteRationalSet:
    #premesso che esiste un isomorfismo fra numeri razionali e numeri reali con parte decimale finita,
    #==> i numeri esprimibili da un calcolatore di tipo float sono un sottoinsieme dei razionali
    def __init__(self, notInSet):
        self.notInSet = notInSet
        self.min = -1000
        self.max = 1000
    def hasIn(self, element):

        if (type(element) == float or type(element) == int) and (element not in self.notInSet):
            return True
        else:
            return False

    def randomSample(self):

        return [random.uniform(self.min, self.max) for i in range(0, 100)]

# class RationalSet:
#     # the bigger is max the more dense and so near true Q the set RationalSetPositive becomes--density not uniform
#     def __init__(self, max):
#         self.orign = IntegerSet(-max, max)
#
#     def __iter__(self):
#         self.perm = itertools.permutations(self.orign, 2)
#         self.cache = [0]
#         return self
#
#     def __next__(self):
#         while True:
#             x, y = next(self.perm)
#             r = x/y
#             if r not in self.cache: break
#
#         self.cache.append(r)
#         return self.cache[-2]
#
#     def extra_elements(self, n_operands):
#         return

class CompositionPerm:
    def __init__(self, identity):
        self.identity = identity

    def composition(self, x1, x2):
        i = [ x1.index(p) for p in self.identity ]
        res = [1,1,1]
        for curr in range(0, len(x2)):
            res[ i[curr] ] = x2[curr]

        return tuple(res)

class ModularSum:
    def __init__(self, cardinality):
        self.card = cardinality

    def sum(self, x, y):
        return (x+y)%self.card

if __name__ == '__main__':
    import operator

    m1 = Monoid( set = {True, False}, operation = operator.or_, i = False )
    print( m1 )
    print( "add = logic or:" )
    print( "add(True, False) = {0}".format(m1.add(True, False)) )
    print( "add(False, True) = {0}".format(m1.add(False, False)) )
    print( "add(True, True) = {0}".format(m1.add(True, True)) )

    print("////////////////////////////////////////////////////")
    s = {0,1,2,3,4,5,6}
    m2 = Monoid( set = s, operation = ModularSum( len(s) ).sum, i = 0 )
    print( m2 )
    print( "add = (a+b)%cardinality:" )
    print( "add({0},{1}) = {2}".format(1, 2, m2.add(1, 2)) )
    print( "add({0},{1}) = {2}".format(4, 5, m2.add(4, 5)) )
    print( "add({0},{1}) = {2}".format(1, 0, m2.add(1, 0)) )
    print( "add({0},{1}) = {2}".format(6, 1, m2.add(6, 1)) )

    print("////////////////////////////////////////////////////")
    s = set(itertools.permutations('RGB')) #set all tuples permutations of ('R', 'G', 'B')
    g1 = Group( set = s, operation = CompositionPerm(tuple('RGB')).composition, i = tuple('RGB') )
    print( g1 )
    print( "add = composition of permutation, e.g: (R, B, G) o (B, G, R) = (B, R, G)")
    print( "{0} o {1} = {2}".format(tuple('RBG'), tuple('BGR'), g1.add(tuple('RBG'), tuple('BGR'))) )
    print( "{0} o {1} = {2}".format(tuple('RGB'), tuple('BGR'), g1.add(tuple('RGB'), tuple('BGR'))) )
    print( "{0} o {1} = {2}".format(tuple('GBR'), tuple('BGR'), g1.add(tuple('GBR'), tuple('BGR'))) )
    print( "{0} o {1} = {2}".format(tuple('GRB'), tuple('RGB'), g1.add(tuple('GRB'), tuple('RGB'))) )


    # q = RationalSetPositive(100)
    # for x in q:
    #     print(x)
    #
    # t = Group( set = q, operation = operator.mul, i = 1)