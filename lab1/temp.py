def table(x):
    l = [['C',x], ['F',x*(9/5) +32], ['K',x+273.15], ['Ra',(x+273.15)*(9/5)], ['D',(100-x)*(3/2)], ['N',x*(33/100)], ['Re',x*(4/5)], ['Ro',x*(21/40) +7.5]]
    s = "Tabella temp value " + str(x) + "\n"
    for y in l: s += "{0}-->{1}\n".format(y[0], y[1])
    return s

def toAll(x):
    temp = {'F':(x[1]-32)*(5/9), 'K':x[1]-273.15, 'Ra':(x[1]-491.67)*(5/9), 'D':100-x[1]*(2/3), 'N':x[1]*(100/33), 'Re':x[1]*(5/4), 'Ro':(x[1]-7.5)*(40/41)}
    return table(temp[x[0]])


x = ['F', 25]
print(toAll(x))
    

