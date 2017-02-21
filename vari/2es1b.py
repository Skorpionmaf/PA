import functools
import collections
def and_logico(x, y): return(x and y)

def is_prime(x, start = 2):
    if x==1 or start == x:
        return True
    elif x%start == 0:
        return False
    else:
        start = start + 1
        return( is_prime(x, start) )

def prime_decomposition(x, start = 2, fact = [1] ):
    if functools.reduce(lambda z, y: z*y, fact) == x:
        return fact
    elif is_prime( start ) and (x/functools.reduce(lambda x, y: x*y, fact))%start==0:
        fact.append(start)
        return prime_decomposition(x, start+1, fact)
    elif start == x+1:
        start = 2
        return prime_decomposition(x, start, fact)
    else:
        return prime_decomposition(x, start+1, fact)


divisori = [x for x in range(1,21)]

dec = [prime_decomposition(x, start=2, fact=[1]) for x in divisori]

cnt = [collections.Counter(x) for x in dec]

fact = { k:0 for k in range(1, 21) if is_prime(k) }

fact_n = [ ]
print(fact)
for x in cnt:
    for k in x.keys():
        if x[k] > fact[k]:
            fact[k] = x[k]

print(fact)

l = [ pow(k, fact_n[k]) for k in fact_n.keys() ]
res = functools.reduce(lambda x, y: x*y, l)

print( res )
    
