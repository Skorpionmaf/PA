import functools

def tre_o_cinque(x): return( (x%3)==0 or (x%5)==0 )

numbers = [x for x in range(1, 1001)]

filter_numbers = list(filter(tre_o_cinque, numbers))

total = functools.reduce(lambda x, y: x+y, filter_numbers)

print(total)
