
def KIWC(file): #it returns a list of lines properly formatted

    f = open(file, mode = 'r')
    l = []
    i = 1
    for line in f:
        l.append( (line.strip(), i) )
        i += 1

    extra = ['the', 'is', 'a', 'an', 'then', 'although', 'instead', 'are', 'because']

    words = { w:line for line in l for w in line[0].split() if w.lower() not in extra}
    ref = { w.lower():w for w in words.keys() }

    out = []
    for w in sorted(ref.keys()):
        p1 = words[ref[w]][0].split(ref[w])[0].strip()
        p2 = words[ref[w]][0].split(ref[w])[1].strip()

        if len(p1) > 33:
            p1 = p1[-33:]

        s = str( words[ref[w]][1] ).rjust(5) + ' ' + p1.rjust(40 -2 - 5) + ' ' + ref[w] + ' '

        if len(p2) > (79-len(s)-1):
            p2 = p2[:(79-len(s)-1)]

        s += p2.ljust(79-len(s)-1) + '.'
        out.append(s)
        print(s)

    return out

