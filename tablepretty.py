
def pretty(file):
    fr = open(file, "r")
    content = [l.strip().split(';') for l in fr]
    content = [ [w.strip() for w in l] for l in content]

    space = { k:0 for k in range(len(content[0])) }
    for k in space.keys(): space[k] = max( list(map(len, [content[i][k] for i in range(len(content))] )) )

    n_col = len( content[0] )
    totspace = n_col + 1 + 2*n_col + sum(space.values())
    sep = "".join(['-' for i in range(totspace)])

    just = [ [l[k].ljust(space[k]) for k in range(len(l))] for l in content ]

    out = [ "| " + " | ".join( l ) + ' |' for l in just ]

    out.insert(0, sep)
    out.insert(2, sep)

    for l in out: print(l)
