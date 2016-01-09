import time

def memoization(F):
    def wrapper(*args):
        obj = args[0]
        if 'results' not in obj.__dict__:
            obj.results = dict()

        if args[1:] not in obj.results.keys():
            print("\ncalculating the result...")
            obj.results[ args[1:] ] = F(*args)
        else:
            print("\nfetching already computed result...")

        return obj.results[ args[1:] ]
    return wrapper

def timer(F):
    def wrapper(*args):
        start = time.clock()
        res = F(*args)
        finish = time.clock()
        elapsed = finish - start

        print("\nelapsed time-->{0}".format(elapsed))

        return res
    return wrapper

def logging(F):
    def wrapper(*args):
        of = open("log_" + F.__name__, "w")
        of.write("\nmethod name: {0}".format(F.__name__))
        for i in range(0, len(args)):
            of.write('\n{0} --> {1}'.format(F.__code__.co_varnames[i], args[i]) )

        res = F(*args)
        of.write("result" + str(res))

        return res
    return wrapper

class MyMath:

    @memoization
    @logging
    def fib(self, start_value, n_terms):

        l = [start_value, start_value]
        for x in range(0, n_terms):
            l.append(l[-1] + l[-2])

        return l

    @memoization
    @logging
    def fact(self, n):

        res = 1
        for x in range(2, n+1):
            res *= x

        return res

    def deriv(self, dx, f, a, order):

        if order == 1:
            return (f(a+dx) - f(a)) / dx
        else:
            return (self.deriv(dx, f, a + dx, order-1) - self.deriv(dx, f, a, order-1)) / (dx)

    @memoization
    @logging
    def taylor(self, f, x, a, order, precision = 0.01):
        dx = precision

        res = f(a)
        s = str( f(a) )
        for i  in range(1, order+1):
            deriv = self.deriv(dx, f, a, i)
            incr = (x - a)**i
            fac = self.fact(i)

            res += deriv * incr / fac
            s += ' + ' + str( deriv / fac ) + ' * ' + '(' + str(x) + ' - ' + str(a) + ')' + '**' + str(i)

        print(s)
        return res




