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

    return check_rings

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

ring_z = make_ring(Z, Z(0), lambda x, y: Z(x.value + y.value), Z(1), lambda x, y: Z(x.value * y.value))
test_z = make_tests(ring_z, "(Z, +, ×)")

all_tests = [test_z]
suite = unittest.TestSuite()

if __name__ == "__main__":
    for tc in all_tests:
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tc))

    unittest.TextTestRunner(verbosity=2).run(suite)
