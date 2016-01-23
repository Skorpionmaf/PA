import threading, functools

def input(l, n_thds):
    sub_set = int(len(l) / n_thds )
    orig = l[:]
    input = [ [orig.pop() for j in range(sub_set)] for i in range(n_thds) ]

    extra = len(l) - sub_set*n_thds
    ext = [orig.pop() for i in range(extra)]
    if ext != []:
        input.append( ext )

    return input

def split_and_merge(n_thds, recomposition_fun):
    def decorator(F):
        thread_res = []

        def th(sub_list):
            thread_res.append(F(sub_list))

        def wrapper(*args):
            inp = input(args[0], n_thds)
            tds = [ threading.Thread(target=th, args=(sl,)) for sl in inp ]

            for t in tds: t.start()

            for t in tds: t.join()
            print('All Threads have finished')

            return recomposition_fun(thread_res)
        return wrapper
    return decorator

@split_and_merge(2, lambda a: functools.reduce(lambda x, y: x*y, a))
def mul(l):
    return functools.reduce(lambda x, y: x*y, l)


if __name__ == '__main__':
    print(mul( [1, 2, 3, 4, 1, 1, 2] ))



