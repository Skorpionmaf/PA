import unittest

def make_ring(S, z, op1, i, op2):
    S.i = i
    S.z = z
    S.__add__ = op1
    S.__mul__ = op2
    return S

def make_tests(ring, name):
    class check_rings(unittest.TestCase):
        def test_closure(self):
            print("### Checking Closure on {0}: ".format(name))
            checks = [ (x + y).inSet() and (x * y).inSet() for x in ring.signature() for y in ring.signature()]
            self.assertTrue(all(checks), msg="The ring does not respect closure property: ")

        def test_sum_associativity(self):
            print("### Checking Sum Associativity on {0}: ".format(name))
            checks = [ ((x + y) + z) == (x + (y + z)) for x in ring.signature() for y in ring.signature() for z in ring.signature()]
            self.assertTrue(all(checks), msg="The ring does not respect associativity prop. for the addition: ")

        def test_mul_associativity(self):
            print("### Checking Mul Associativity on {0}: ".format(name))
            checks = [ ((x * y) * z) == (x * (y * z)) for x in ring.signature() for y in ring.signature() for z in ring.signature()]
            self.assertTrue(all(checks), msg="The ring does not respect associativity multiplication: ")

        def test_sum_identity(self):
            print("### Checking Sum Identity {1} on {0}: ".format(name, ring.z))
            checks = [ring.z in ring.signature()]
            for x in ring.signature(): checks += [(ring.z + x) == x]
            self.assertTrue(all(checks), msg="The ring does not respect the identity property for the addition: ")

        def test_mul_identity(self):
            print("### Checking Mul. Identity {0} on {1}: ".format(name, ring.i))
            checks = [(ring.i * x) == x for x in ring.signature()] + [ring.i in ring.signature()]
            self.assertTrue(all(checks), msg="The ring does not respect the identity for the multiplication: ")

        def test_invertibility(self):
            print("### Checking Sum Invertibility on {0}: ".format(name))
            checks = []
            for x in ring.signature():
                checks += [any([(x + y) == ring.z for y in ring.signature()])]
            self.assertTrue(all(checks), msg="The ring does not respect invertibility property for the addition: ")

        def test_sum_commutativity(self):
            print("### Checking Sum Commutativity on {0}: ".format(name))
            checks = [(x + y == y + x) for x in ring.signature() for y in ring.signature()]
            self.assertTrue(all(checks), msg="The ring does not respect commutativity property for the addition: ")

        def test_left_distributivity(self):
            print("### Checking Left Distributivity of Mul over Sum on {0}: ".format(name))
            checks = [(x * (y + z) == (x * y) + (x * z)) for x in ring.signature() for y in ring.signature() for z in ring.signature()]
            self.assertTrue(all(checks), msg="The ring does not respect left distributivity of multiplication over addition: ")

        def test_right_distributivity(self):
            print("### Checking Right Distributivity of Mul over Sum on {0}: ".format(name))
            checks = [((y + z) * x == (y * x) + (z * x)) for x in ring.signature() for y in ring.signature() for z in ring.signature()]
            self.assertTrue(all(checks), msg="The ring does not respect left  distributivity of multiplication over addition: ")

    return check_rings

# def nzgen():
#     val = 0
#     yield nZ(val)
#     while True:
#         val += 1
#         yield nZ(val)
#         yield nZ(-val)

def zgen():
    val = 0
    yield Z(val)
    while True:
        val += 1
        yield Z(val)
        yield Z(-val)

class Z:
    def __init__(self, val): self.value = val

    def __eq__(self, other): return self.value == other.value

    def __repr__(self): return str(self.value)

    def signature(n=50): return [Z(x) for x in range(-n, n + 1)]

    def inSet(self): return (self in zgen())


# class Z4:
#     def __init__(self, val): self.value = val
#
#     def __eq__(self, other): return self.value == other.value
#
#     def __repr__(self): return str(self.value)
#
#     def signature(): return [Z4(x) for x in [0, 1, 2, 3]]
#
#     def inSet(self): return (self in Z4.signature())
#
#
# class B:
#     def __init__(self, val): self.value = val
#
#     def __eq__(self, other): return self.value == other.value
#
#     def __repr__(self): return "True" if self.value == 1 else "False"
#
#     def signature(): return [B(x) for x in range(2)]
#
#     def inSet(self): return (self in B.signature())
#
#
# class nZ:
#     def __init__(self, val): self.value = val
#
#     def __eq__(self, other): return self.value == other.value
#
#     def __repr__(self): return str(self.value)
#
#     def signature(n=50): return [nZ(x) for x in range(-n, n + 1)]
#
#     def inSet(self): return (self in zgen())


# nonring_bool = make_ring(B, B(0), lambda x, y: B(x.value | y.value), B(1), lambda x, y: B(x.value & y.value))
# test_bool = make_tests(nonring_bool, "(Bool, ∨, ∧)")

ring_z = make_ring(Z, Z(0), lambda x, y: Z(x.value + y.value), Z(1), lambda x, y: Z(x.value * y.value))
test_z = make_tests(ring_z, "(Z, +, ×)")

# nonring_z = make_ring(nZ, nZ(1), lambda x, y: nZ(x.value * y.value), nZ(0), lambda x, y: nZ(x.value + y.value))
# test_nz = make_tests(nonring_z, "(Z, ×, +)")
#
# ring_z4 = make_ring(Z4, Z4(0), lambda x, y: Z4((x.value + y.value) % 4), Z4(1), lambda x, y: Z4((x.value * y.value) % 4))
# test_z4 = make_tests(ring_z4, "(Z₄, +₄, ×₄)")

# all_tests = [test_z, test_nz, test_z4, test_bool]

all_tests = [test_z]
suite = unittest.TestSuite()

if __name__ == "__main__":
    for tc in all_tests:
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tc))
    unittest.TextTestRunner(verbosity=2).run(suite)
