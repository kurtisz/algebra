from fractions import gcd
from itertools import product
import core
from core import NullaryOperation, UnaryOperation, BinaryOperation

class Magma(object):
    def __init__(self, elements, function):
        for a in elements:
            for b in elements:
                if not function(a, b) in elements:
                    raise ValueError("({0}, {1}) -> {2} is not closed".format(a, b, function(a, b)))
        try:
            self._domain = set(elements)
        except:
            self._domain = elements
        self._operation = BinaryOperation(self._domain, function)
        
    def __iter__(self):
        for a in self._domain:
            yield a
    
    def add(self, a, b):
        return self._operation.eval(a, b)

def getIdentity(S, fxy):
    for a in S:
        isIdentity = True
        for b in S:
            if not fxy(a, b) == b:
                isIdentity = False
                break
        if isIdentity:
            return a
    return None

def haveInverses(S, fxy, e):
    return reduce(lambda x, y : x and y, map(lambda a :hasInverse(a, S, fxy, e), S))

def hasInverse(a, S, fxy, e):
    for b in S:
        if fxy(a, b) == e:
            return True
    return False

def getInverse(a, S, fxy, e):
    for b in S:
        if fxy(a, b) == e:
            return b
    return None

class Group(Magma):
    def __init__(self, elements, function):
        super(Group, self).__init__(elements, function)
        self._order = len(self._domain)
        e = getIdentity(elements, function)
        if e is None:
            raise ValueError("Set has no identity under given function")
        self._e = NullaryOperation(e)
        if not haveInverses(elements, function, e):
            raise ValueError("Set elements do not all have an inverse")
        self._inverse = UnaryOperation(elements, lambda x : getInverse(x, elements, function, e))
    
    def __len__(self):
        return self._order
    
    def invert(self, a):
        return self._inverse.eval(a)
    
    def identity(self):
        return self._e.eval()
    
    def isSubgroup(self, H):
        if len(H) > len(self):
            return False
        if len(H) == len(self):
            return H == self
        for a in H:
            if not a in self._domain:
                return False
        return True
        ''' Having trouble proving equality of operations
            Need a way to have an operation from Integers -> subset of Integers (for the mod operations, for example)
            Then need to be able to prove equality
        '''
        return H._operation == self._operation
    
    def __eq__(self, other):
        return other._domain == self._domain and other._operation == self._operation

class Integers(Group):
    def __init__(self):
        super(Z, self).__init__(core.Integers, lambda x, y : x + y)
    
    def __str__(self):
        return "Z"
    
    def __eq__(self, other):
        return type(other) == type(self)

class Z(Group):
    def __init__(self, n):
        if not type(n) == int or n <= 0:
            raise ValueError("Z_{0} is undefined".format(n))
        super(Z, self).__init__([i for i in range(n)], lambda x, y : (x + y) % n)
    
    def __str__(self):
        return "Z_{0}".format(self._order)

class U(Group):
    def __init__(self, n):
        if n <= 0 or not type(n) == int:
            raise ValueError("U_{0} is undefined".format(n))
        super(U, self).__init__([i for i in range(n) if gcd(i,n) == 1], lambda x, y : (x * y) % n)
        self._n = n
    
    def __str__(self):
        return "U_{0}".format(self._n)

class DirectSum(Group):
    def __init__(self, *groups):
        self._groups = groups
        groupSets = map(lambda G : [x for x in G], groups)
        elements = [x for x in product(*groupSets)]
        function = lambda x, y : tuple([groups[i].add(x[i], y[i]) for i in range(len(groups))])
        super(DirectSum, self).__init__(elements, function)
    
    def __str__(self):
        s = str(self._groups[0])
        for G in self._groups[1:]:
            s += " + " + str(G)
        return s

def getCosets(G, H):
    foundCosets = []
    cosets = []
    for a in G:
        aCoset = set([G.add(a, h) for h in H])
        if aCoset in foundCosets:
            coset = [c for c in cosets if c[2] == aCoset][0]
            coset[1].add(a)
        else:
            foundCosets.append(aCoset)
            cosets.append([a, set([a]), aCoset])
    return map(lambda x : tuple(x), cosets)

class FactorGroup(Group):
    def __init__(self, G, H):
        if not G.isSubgroup(H):
            raise ValueError("{0} is not a subgroup of {1}".format(H, G))
        self._G = G
        self._H = H
        cosets = getCosets(G, H)
        super(FactorGroup, self).__init__(cosets, lambda x, y : [a for a in cosets if self._G.add(x[0], y[0]) in a[1]][0])
    
    def __str__(self):
        return str(self._G) + " / " + str(self._H)