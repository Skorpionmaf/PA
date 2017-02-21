import functools, timeit

def compact_join(l, res, current, count):
  if l == []: return res+('' if count == 0 else str(count+1))+current
  if l[0] == current: return compact_join(l[1:], res, current, count+1)
  else: return compact_join(l[1:],
    res+('' if count == 0 else str(count+1))+current, l[0], 0)

def hash(w):
  return compact_join(sorted(w.lower()), '', '', 0)

#words = dict()

def organize(fn, words):
  for w in open(fn).read().split():
    h = hash(w)
    if h in words.keys():
      words[h] += [w]
    else: words[h] = [w]
  return words

def find_out():
  words = organize('wordlist-anagram.txt', dict())
  return {k:w for (k,w) in words.items() if len(w) > 1}

def anagrams():
  anag = find_out()
  tmp = {w[0]: sorted(w[1:], key=str.lower)
     for (k,w) in anag.items() if len(w)>2}
  return functools.reduce(
    lambda x,y:x+y,
      [("{:12} :- {}"+((len(tmp[k])-1)*", {}")+"\n").format(k, *tmp[k])
         for k in sorted(tmp.keys(), key=str.lower)])

def anagram(w):
  anag = find_out()
  tmp = hash(w)
  if tmp in anag.keys():
    res = sorted(list(set(anag[tmp]).difference({w})), key=str.lower)
    return ("{}"+(len(res)-1)*", {}").format(*res)
  else: return "None"

if __name__ == '__main__':

    print("execution of anagrams of Cazzola")
    start = timeit.timeit()
    anagrams()
    end = timeit.timeit()

    print(end - start)