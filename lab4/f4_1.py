
class my_str(str):

    def isPalindroma(self):
        l = []
        for el in self:
            if el.isalpha():
                l.append(el.lower())

        isp = True
        for i in range(0, int(len(l)/2) ):
            if l[i] != l[-(i+1)]:
                isp = False

        return isp

    def __sub__(self, other):
        p = list(other)
        l = ""
        for el in self:
            if (el in p) == False:
                l += el

        return my_str(l)

    def anagram(self, l):
        r = []
        for el in l:
            if len(el) == len(self):
                t = list(el)
                for let in self:
                    if let in t:
                        t.remove(let)
                    else:
                        break
                if ( len(t) == 0 ):
                    r.append(el)

        return r

if __name__ == "__main__":
    s = my_str("Ciao")
    p = my_str("a")
    t = s - p
    print(t)