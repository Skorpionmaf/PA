# Another type of problem
def words_dict_gen(path = '/usr/share/dict/words'):
    f = open(path, "r")
    words_dict = dict()

    for l in f:
        w = l.strip()
        w_l = "".join( sorted(list(l.strip())) )
        if w_l in words_dict.keys():
            words_dict[w_l].append( w )
        else:
            words_dict[w_l] = []

    return words_dict

def anagram(word, words_dict = dict()):
    if len(words_dict) == 0:
        words_dict = words_dict_gen()

    word = word.lower()
    word_sorted = "".join( sorted(list(word)) )

    if word_sorted in words_dict.keys():
        return [ x for x in words_dict[word_sorted] if x != word ]
    else:
        return []

def anagrams():
    words_dict = words_dict_gen()

    path_list = './wordlist-anagram.txt'
    fr = open(path_list, "r")

    cache = []
    fw = open('./output.txt', "w")
    for w in ( l.strip() for l in fr ):
        al = anagram(w, words_dict)
        if len(al) >= 2 and w not in cache:
            print( w.ljust(10) + ':-        ' + str(al) )
            fw.write("{0}   :-      {1}\n".format(w.ljust(10), al) )

            cache.append(w)
            for x in al: cache.append(x)






