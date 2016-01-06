
class SocialNet:

    def __init__(self, vertexList, tupleList = []):

        self.graph = {}

        for el in vertexList:
            self.graph[el] = []

        if len(tupleList) > 0:
            self.addAllLinks(tupleList)

    def addLink(self, node1, node2):

        self.graph[node1].append(node2)
        self.graph[node1].sort()

        self.graph[node2].append(node1)
        self.graph[node2].sort()

    def addAllLinks(self, tupleList):

        for t in tupleList:
            self.addLink(t[0], t[1])

    def nodeDegree(self, node):

        return len( self.graph[node] )

    def avgDegree(self):

        deg = ( len(self.graph[node]) for node in self.graph )

        s = 0
        l = 0
        for el in deg:
            s += el
            l += 1

        s /= 2
        l /= 2

        return s/l

    def degDistribution(self):

        deg = [ len(self.graph[node]) for node in self.graph ]

        m = min(deg)
        M = max(deg)

        bin = (M - m) * 0.1

        p = {}
        t = m
        while t <= M:
            p[t, t + bin] = 0
            t += bin

        for d in deg:
            for b in p.keys():
                if d >= b[0] and d < b[1]:
                    p[b[0], b[1]] += 1

        return p

    def __str__(self):
        s = ""
        for el in self.graph:
            s += str(el)
            s += ": "
            s += str(self.graph[el])
            s += "\n"

        return s