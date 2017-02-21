import unittest

def make_ring(R, z, op1, i, op2):
    R.z = z
    R.i = i
    R.__add__ = op1
    R.__mul__ = op2
    return R

def test_ring(ring, name):
    class check_all(unittest.TestCase):
        def test_closure_sum(self):
            print("### Checking Closure for the sum on {0}: ".format(name))
            checks = [ (x+y).inSet() for x in ring.elements() for y in ring.elements() ]
            self.assertTrue( all(checks), msg='Closure property violated for sum')

    return check_all

def z_gen():
    x = 0
    yield Z(x)
    while True:
        x += 1
        yield Z(x)
        yield Z(-x)

class Z:
    def __init__ (self, val): self.val = val

    def __eq__(self, other): return self.val == other.val

    def __repr__(self): return str(self.val)

    def elements(n=50): return [Z(x) for x in range(-n, n+1)]

    def inSet(self): return (self in z_gen())

ring1 = make_ring(Z, Z(0), lambda x, y: Z(x.val+y.val), Z(1), lambda x, y: Z(x.val*y.val))
tc1 = test_ring(ring1, "Z")

all_tests = [tc1]
suite = unittest.TestSuite()

if __name__ == "__main__":
    print( ring1.elements() )
    for tc in all_tests:
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tc))

    unittest.TextTestRunner(verbosity=2).run(suite)
