
words = [w for w in open('wordlist-7.txt').read().split()]

def eqm1(w1, w2):
    return [w1[i]==w2[i] for i in range(len(w1))].count(False)==1

def organize(n):
    ws = {w:[] for w in words if len(w)==n}
    for elem in dict.keys(ws):
        ws[elem] = sorted([e for e in dict.keys(ws) if eqm1(elem, e)])
    return ws

w7 = organize(7)

def flatten(l):
    res = []
    for el in l:
        if all(isinstance(ell, str) for ell in el):
            #print('ciao1')
            res = res + [el]
            #print(res)
        else:
            #print('ciao2')
            res = res + flatten(el)
            #print(res)
    return res

def chain(ws,wt):
    def chainr(ws, wt, path):
        if ws == wt: return path+[ws]
        if w7[ws] == []: return []
        return flatten([l for l in
            [chainr(w, wt, path+[ws]) for w in w7[ws] if not (w in path)]
            if l != []])
    res = sorted(flatten([l for l in
        [chainr(w,wt,[ws]) for w in w7[ws]] if l != []]))
    return (len(res)*"{}\n").format(*res)