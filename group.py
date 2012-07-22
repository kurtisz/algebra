from fractions import gcd
from groupUtils import getIdentity, getInverse, getOrder, commutes

class Element(object):
    def __init__(self, value, op):
        self._value = value
        self._op = op
        self._inverse = None
        self._order = 0
        
    def __add__(self, other):
        return self._op(self._value, other._value)
    
    def __str__(self):
        return str(self._value)
    
    def __eq__(self, other):
        return self._value == other._value
    
    def __neg__(self):
        return self._inverse
    
    def __len__(self):
        return self._order
    
    def generateCyclicSubgroup(self):
        # returns a list of elements in subgroup
        H = []
        cum = a
        for i in range(self._order):
            H.append(cum)
            cum = cum + a
        return H

class Group(object):        
    def __init__(self, elements, operation):
        self._operation = lambda x, y: self._elements[operation(x,y)]
        self._identity = getIdentity(elements, operation)
        self._elements = {e:Element(e, self._operation) for e in elements}
        for e in self:
            e._inverse = self._elements[getInverse(e._value, elements, operation, self._identity)]
            e._order = getOrder(e._value, operation, self._identity, len(elements))
    
    def __len__(self):
        # the "order" of the group
        return len(self._elements)
    
    def __iter__(self):
        for key in sorted(self._elements.keys()):
            yield self._elements[key]
    
    def __contains__(self, a):
        return a in self._elements.values()
    
    def __getitem__(self, a):
        return self._elements[a]
    
    def identity(self):
        return self._elements[self._identity]
    
    def center(self):
        c = []
        for a in self:
            if commutes(a, self):
                c.append(a)
        return c

class Z(Group):
    def __init__(self, n):
        super(Z, self).__init__(list(range(n)), lambda x, y : (x + y) % n)

class U(Group):
    def __init__(self, n):
        super(U, self).__init__([i for i in range(1,n) if gcd(i,n) == 1], lambda x, y : (x * y) % n)

if __name__ == '__main__':
    Z5 = Z(8)
    print len(Z5)
    print [str(i) for i in Z5.center()]
    for a in Z5:
        print a, -a
        print [str(i) for i in a.generateCyclicSubgroup()]