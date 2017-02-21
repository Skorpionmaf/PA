import permutations

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

w_dict = words_dict('./wordlist7.txt')

def recursive_word_find(word, end, index, cars):

    if index < len(end) and word[index] == end[index]:
        return recursive_word_find(word, end, index+1, cars)

    elif index == len(end):
        pass

    else:
        word = list(word)
        head_c = word.pop(0)

        if len(cars) == 0:
            cars = [c for c in range_cars('a', 'z')]
            return recursive_word_find(word, end, index+1, cars)

        else:
            c = cars.pop()
            if c != head_c:
                word.insert(index, c)

            s = "".join(word)
            if s in w_dict:
                print(s)



def chain(start, end):

    cars_set = {c for c in range_cars('a', 'z')}
    # ws = [ start[i] for i in range(0, len(start)) if start[i] == end[i] ]

    recursive_word_find(start, end, 0, cars_set)
