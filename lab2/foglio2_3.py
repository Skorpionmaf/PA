import itertools

def fact_my(n):

    res, mult = 1, 0

    while mult < n:
        yield mult, res
        mult += 1
        res *= mult

def sin_my(x, n):
    el = ( pow(x, f[0])/f[1] for f in fact_my(n*2) if f[0]%2 != 0 )
    el2 = ( x[1] * pow(-1, x[0]) for x in enumerate(el) )

    return sum(el2)

if __name__ == '__main__':
    import math

    for x in range(1, 5):
        print('math sin({0})'.format(x))
        print(math.sin(x))
        for n in range(1, 11):
            print('series of sine with {0} terms in x={1}'.format(n, x))
            print(sin_my(x, n))
        print()