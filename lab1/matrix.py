def identity(n):
    return [ [(1 if i==j else 0) for j in range(0,n)] for i in range(0,n) ]

def square(n):
    return [ [(n*i+j + 1) for j in range(0,n)] for i in range(0,n) ]

def transpose(matrix):
    return [ [matrix[i][j] for i in range(0, len(matrix))] for j in range(0,len(matrix[0])) ]

def multiply(m1, m2):
    import functools
    return [ [ functools.reduce(lambda x, y : x+y, [m1[i][x]*m2[x][j] for x in range(0,len(m2))]) for j in range(0,len(m2[0]))] for i in range(0,len(m1)) ] 


print(square(2))
print(multiply(square(2), square(2)))
