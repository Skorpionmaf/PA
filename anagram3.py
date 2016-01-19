import timeit

def words_dict_gen(path = './wordlist-anagram.txt'):
    words_dict = dict()

    f = open(path, "r")
    for l in f:
        w = l.strip()
        w_l = "".join( sorted(list(w.lower())) )
        if w_l in words_dict.keys():
            words_dict[w_l].append( w )
        else:
            words_dict[w_l] = [w]

    return words_dict

def anagram(word, words_dict = {}):
    if len(words_dict) == 0:
        words_dict = words_dict_gen()

    word = word.lower()
    word_sorted = "".join( sorted(list(word)) )

    if word_sorted in words_dict.keys():
        return  words_dict[word_sorted]
    else:
        return []


def anagrams():
    words_dict = words_dict_gen()

    #path_out = './output.txt'
    #fw = open(path_out, "w")

    new_dict = { w[0]:sorted(w[1:], key = str.lower) for w in words_dict.values() if len(w)>2 }
    cache = []
    res = []
    for k in sorted(new_dict.keys(), key = str.lower):
        w = new_dict[k]
        if k not in cache:
            s = ("{:12}   :-      {}" + (len(w) -1)*" {}").format(k.ljust(10), *w)
            #fw.write( s + '\n')
            res.append(s)

            cache.append(k)
            for x in w: cache.append(x)

    return res

if __name__ == '__main__':
    print("execution of Mio anagrams")
    start = timeit.timeit()
    anagrams()
    end = timeit.timeit()

    print(end - start)