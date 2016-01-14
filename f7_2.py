
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(2, n):
        if n%i == 0:
            return False

    return True

def prime_list(n):

    return [p for p in range(2, n) if is_prime(p)]

def golbach(n):

    for x in prime_list(n):
        if is_prime(n-x):
            return (x, n-x)

    return 'no golbach partition exixsts for {0}'.format(n)

def golbach_list(n, m):

    return { x:golbach(x) for x in range(n, m+1) if x > 2 and x%2 == 0 }


