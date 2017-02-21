import functools
import collections

# ritorna True se x e' primo
def is_prime(x):
    numbers = [n for n in range(1, x+1)]
    test = list(map(lambda n: x%n == 0, numbers))
    return collections.Counter( test )[True] == 2 or x == 1

# ritorna la lista dei divisori di x che sono primi
def prime_divisori(x):
    numbers = [n for n in range(1, x+1)]
    return [ n for n in numbers if is_prime(n) and x%n == 0 ]

# ritorna oggetto class counter (si accede come in un dizionario) che rappresenta il numero scomposto in fattori primi es: se viene passato 12 ritorna Counter({2:2, 3:1}) --> (2^2) * (3^1)
def prime_decomposition(x, fact = []):
    div = prime_divisori(x)
    fact.append( max(div) )
    return ( x//max(div)==1 and collections.Counter(fact) ) or prime_decomposition( x//max(div), fact)

# viene creato un dizionario che associa ad ogni numero 1:20 la sua scomposizione in fattori primi
n_list = { x:prime_decomposition(x, []) for x in range(1,21) }

# crea dizionario con chiave = fattore primo, valore = esponente
fact = { k:0 for k in range(1, 21) if is_prime(k) }

# per ogni fattore primo si cerca l'esponente massimo con cui compare nelle scomposizioni in fattore primi dei numeri da 1:20
for x in n_list.values():
    for k in x.keys():
        if x[k] > fact[k]:
            fact[k] = x[k]
# ??? Come miglioro questi due for che non vanno bene in programmazione funzionale? idee?

l = [ pow(k, fact[k]) for k in fact.keys() ]
res = functools.reduce(lambda x, y: x*y, l)
print( res )