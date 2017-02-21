import copy

def diff1(string1, string2):
    return True if sum([0 if list(string1)[i] == list(string2)[i] else 1 for i in range(len(string1))]) == 1 else False

listOfWords = [word for word in open("./wordlist-7.txt", 'r').read().split()]
#print(listOfWords)

def chain(string1, string2):
    listofmatch = chainr(string1, string2, listOfWords, [], [])
    string = ""
    for array in listofmatch:
        string += str(array)+"\n"
    return string

def chainr(string1, string2, listOfWords, lista, listOfList):
    if string1 == string2:
        lista.append(string1)
        listOfList.append(lista)
    listOfNext = [elem for elem in listOfWords if diff1(elem, string1)]
    for nextElem in listOfNext:
        newlist = copy.deepcopy(lista)
        newlist.append(string1)
        lWCp = copy.deepcopy(listOfWords)
        lWCp.remove(string1)
        chainr(nextElem, string2, lWCp, newlist, listOfList)
    return listOfList

if __name__ == '__main__':
    print(diff1("warring", "warning"))
    print(diff1("ciao", "ciaa"))
    print(diff1("ciao", "ciaa"))
    print(diff1("ziao", "ciaa"))
    print(diff1("ziao", "ciao"))
    print(diff1("ziao", "ciao"))
    print("### witness → fatness")
    print(chain("witness", "fatness"))
    print("### warning → earring")
    print(chain("warning", "earring"))
    print("### sailing → writing")
    print(chain("sailing", "writing"))
    # print(lista2)