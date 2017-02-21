
def equal_1(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        check = [ (s1[i] == s2[i]) for i in range(0, len(s1)) ]
        check_t = [ x for x in check if not x ]
        return True if len(check_t)==1 else False

def chain(s1, s2, listOfWords):
    result = []
    chainr( s1, s2, listOfWords, [], result)

    for x in result:
        print(x)

def chainr(current_word, s2, avl_words, path, result):
    if current_word == s2:
        path.append( current_word )
        result.append(path)
        return
    else:
        next_words_1 = [w for w in avl_words if equal_1(w, current_word)]
        path.append( current_word )

        for w in next_words_1:
            new_path = path[:]
            new_avl_words = avl_words[:]
            new_avl_words.remove( current_word )

            chainr(w, s2, new_avl_words, new_path, result)
        return

if __name__ == '__main__':
    print( equal_1('ciao', 'pluto') )
    print( equal_1('ciao', 'cibo') )

    listOfWords = [ w for w in open('./wordlist-7.txt', 'r').read().split() ]

    chain('witness', 'fatness', listOfWords)
    chain('warning', 'earring', listOfWords)
    chain('sailing', 'writing', listOfWords)