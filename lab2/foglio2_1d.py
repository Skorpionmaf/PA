def fib(n_digits):
    a, b = 0, 1
    while len(list(str(a))) < n_digits:
        tmp = b
        b = b + a
        a = tmp
        yield a

if __name__ == '__main__':
    l = (x for x in fib(1000))
    print( max(l) )