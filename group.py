from fractions import gcd
from groupUtils import getInverse
from core import Magma, NullaryOperation, Operation

class Loop(Magma):
    def __init__(self, elements, function, identity):
        super(Loop, self).__init__(elements, function)
        self._e = NullaryOperation(identity)
    
    def identity(self):
        return self._e.eval()

class Group(Loop):
    def __init__(self, elements, function, inverseFunction, identity):
        super(Group, self).__init__(elements, function, identity)
        self._inverse = Operation([(x) for x in elements], inverseFunction)
        self._order = len(elements)
    
    def inverse(self, x):
        return self._inverse.eval((x))

class Z(Group):
    def __init__(self, n):
        super(Z, self).__init__(range(n), lambda x, y : (x + y) % n, lambda x : (n - x) % n, 0)
    
    def __str__(self):
        return "Z_{0}".format(self._order)

class U(Group):
    def __init__(self, n):
        S = [i for i in range(1,n) if gcd(i,n) == 1]
        f = lambda x, y : (x * y) % n
        self._n = n
        super(U, self).__init__(S, f, lambda x : getInverse(x, S, f, 1), 1)
    
    def __str__(self):
        return "U_{0}".format(self._n)

if __name__ == '__main__':
    G = U(8)
    print "Group:", G
    print "\tIdentity:", G.identity()
    print "\tInverses:"
    for a in G:
        print "\t\t{0}^(-1) = {1}".format(a, G.inverse(a))
    print "\tCayley table:"
    print "\t\t",
    for a in G:
        print "{0}\t".format(a),
    print
    for a in G:
        print "\t{0}\t".format(a),
        for b in G:
            print "{0}\t".format(G.add(a,b)),
        print