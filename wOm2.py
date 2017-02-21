import functools

def range_cars(car1, car2):
    c = ord(car1)
    while True:
        if c > ord(car2):
            break
        else:
            yield chr(c)
            c += 1

def words_dict(path):
    f = open(path, "r")
    return [ w.strip() for w in f]

w_dict = words_dict('./wordlist-7.txt')
cars_set = [c for c in range_cars('a', 'z')]

def word_find(word, index, cars):
    res = []
    word = list(word)
    original_c = word[index]
    for c in cars:
        if c != original_c:
            word[index] = c
            s = "".join(word)
            if s in w_dict:
                res.append(s)

    return res

# this return a list of all possible words accessible by one letter change
def words_find_allindexes(word, cars):
    list( word )
    l = []
    for index in range(0, len(word)):
        l.append(word_find(word, index, cars_set))

    l_r = list( functools.reduce(lambda x, y: x+y, l) )

    return l_r

def chain(start, end):
    def chainr(start, end, path):
        if start == end: return path+[start]
        if words_find_allindexes(start, cars_set) == []: return []
        return [l for l in [chainr(x, end, path+[start]) for x in words_find_allindexes(start, cars_set) if not (x in path)] if l != []]

    res = [l for l in [chainr(x, end, [start]) for x in words_find_allindexes(start, cars_set)] if l != [] ]
    return res

def flatten(l):
    res = []
    for el in l:
        if all(isinstance(ell, str) for ell in el):
            res = res + [el]
        else:
            res = res + flatten(el)
    return res

def chain2(start, end):
    def chainr(start, end, path):
        if start == end: return path+[start]
        if words_find_allindexes(start, cars_set) == []: return []

        res = []
        for x in words_find_allindexes(start, cars_set):
            print('in R')
            print('start: {0}'.format(start))
            print('x: {0}'.format(x))
            print('path: {0}'.format(path))
            if not (x in path):
                for l in [chainr(x, end, path+[start])]:
                    print('start: {0}'.format(start))
                    if l != []:
                        print(l)
                        res.append(l)
        return flatten(res)

    res = []
    for x in words_find_allindexes(start, cars_set):
        print('in chain')
        print('start: {0}'.format(start))
        print('x: {0}'.format(x))
        for l in [chainr(x, end, [start])]:
            if l != []:
                res.append(l)
    return flatten(res)