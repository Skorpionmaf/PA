import timeit

def words_dict_gen(path = './wordlist-anagram.txt'):
    f = open(path, "r")
    words_dict = dict()

    for l in f:
        w = l.strip()
        w_l = "".join( sorted(list(w.lower())) )
        if w_l in words_dict.keys():
            words_dict[w_l].append( w )
        else:
            words_dict[w_l] = []

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

    path_in = './wordlist-anagram.txt'
    fr = open(path_in, "r")

    path_out = './output.txt'
    fw = open(path_out, "w")

    cache = []
    for w in (l.strip() for l in fr):
        word_sorted = "".join( sorted(list(w.lower())) )

        if len(words_dict[word_sorted]) >= 2 and w not in cache:
            s = "{0}   :-      {1}".format(w.ljust(10), words_dict[word_sorted])
            fw.write( s + '\n')
            cache.append(w)
            for x in words_dict[word_sorted]: cache.append(x)

if  __name__ == '__main__':
    print("execution of anagrams by reading the file two time")
    start = timeit.timeit()
    anagrams()
    end = timeit.timeit()

    print(end - start)