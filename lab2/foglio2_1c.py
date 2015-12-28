import functools

n = pow(2, 1000)
sn = str(n)
l = list(sn)
ln = [int(x) for x in l]

x = functools.reduce(lambda x, y: x+y, ln)

print(x)