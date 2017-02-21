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


def explore(start, end, cache, words_to_explore):
    #print(start)
    step = words_find_allindexes(start, cars_set)

    cache[start] = []
    for x in step: cache[start].append(x)

    for x in step:
        if x not in cache and x not in words_to_explore:
            words_to_explore.append( x )

    #print(step)
    #print(words_to_explore)

    if len(words_to_explore) > 0:
        x = words_to_explore.pop(0)
        explore(x, end, cache, words_to_explore)
    else:
        return cache

    return cache

def build_path(step, end, l, cache, result):
    cache.append
    for x in step[end]:
        build_path(step)

def chain(start, end):
    cache = dict()
    words_to_explore = list()
    step = explore(start, end, cache, words_to_explore)
    print(step)

    l = [end]
    cache = []
    l = build_path(step, end, l)




