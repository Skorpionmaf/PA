import functools
import itertools

def and_logico(x, y): return(x and y)

start = 3*5*7*11*13*17*19
n = [2, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
divisori = [x for x in range(1,21)]

def procedure(start, n, divisori):

    for i in range( 1, len(n) +1 ):
        comb = list(itertools.combinations(n, i))
        for x in comb:
            for el in x:
                start = start * el
            test = [(start%x == 0) for x in divisori]
            res = functools.reduce(and_logico, test)
            if res==True:
                print(i)
                print(x)
                return start
            else:
                for el in x:
                    start = start / el


r = procedure(start, n, divisori)
print(r)




  
