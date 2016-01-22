import threading, functools

class myThread(threading.Thread):
    def __init__(self, thID, name, fun, l):
        threading.Thread.__init__(self)
        self.ID = thID
        self.name = name
        self.method = fun
        self.arg = l
    def run(self):
        print('Starting {0}'.format(self.name))
        self.res = self.method(self.arg)
        print('Finish {0}'.format(self.name))

def split_and_merge(n_thd, recomposition_fun):
    def decorator(F):
        def wrapper(*args):
            n_thds = n_thd
            l = args[0]

            sub_set = int(len(l) / n_thds )
            orig = l[:]
            input = [ [orig.pop() for j in range(sub_set)] for i in range(n_thds) ]

            extra = len(l) - sub_set*n_thds
            ext = [orig.pop() for i in range(extra)]
            if ext != []:
                input.append( ext )
                n_thds = n_thds + 1

            tds = [ myThread(i, 'Thread {0}'.format(i) + ' of ' + F.__name__, F, input[i]) for i in range(n_thds) ]

            for t in tds: t.start()

            for t in tds: t.join()
            print('All Threads have finished')

            results = [ t.res for t in tds ]
            print(results)

            return  recomposition_fun(results)
        return wrapper
    return decorator

@split_and_merge(2, lambda a: functools.reduce(lambda x, y: x*y, a))
def mul(l):
    return functools.reduce(lambda x, y: x*y, l)


if __name__ == '__main__':
    print(mul( [1, 2, 3, 4, 1, 1, 2] ))



