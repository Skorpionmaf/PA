
def memoization(F):
    results = dict()

    def wrapper(*args):
        l = [str(x) for x in args]
        k = ",".join(l)
        if k in results:
            print("caching result for {0}".format(k))
            return results[k]

        r = F(*args)
        results[k] = r
        return r

    return wrapper

@memoization
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

@memoization
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

@memoization
def sum(x, y):
    if x == 0 and y==0:
        return 0
    elif x > 0:
        return 1+sum(x-1, y)
    elif x < 0:
        return -1+sum(x+1, y)
    elif y > 0:
        return 1+sum(x, y-1)
    elif y < 0:
        return -1+sum(x, y+1)