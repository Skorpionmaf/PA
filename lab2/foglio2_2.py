import collections
f = open('testo.txt')

d = dict()
g = (line.strip().split(' ') for line in f)

for w in g:
    for word in w:
        if d.get(word) == None:
            d[word] = 1
        else:
            d[word] = d[word] + 1

print(d)