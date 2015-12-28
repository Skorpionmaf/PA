import re
import collections
f = open('testo.txt')

g = ( line.strip() for line in f )
w = ( re.findall('[a-zA-Z]+|[;:,.]+', x) for x in g )

l = ( x for line in w for x in line )
c = collections.Counter(l)

print( c )
print( c.most_common(3) )