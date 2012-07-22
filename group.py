from fractions import gcd

class Element(object):
    def __init__(self, value, op, group):
        self._value = value
        self._op = lambda y: op(value, y)
        
    def __add__(self, other):
        return self._op(other._value)
    
    def __str__(self):
        return str(self._value)

class Group(object):        
    def __init__(self, elements, operation):
        self._operation = lambda x, y: self._elements[operation(x,y)]
        self._elements = {e:Element(e, self._operation, self) for e in elements}
        self._identity = None
    
    def __iter__(self):
        for key in sorted(self._elements.keys()):
            yield self._elements[key]
    
    def __getitem__(self, key):
        return self._elements[key]
    
    def identity(self):
        if not self._identity:
            for e in self:
                if reduce(lambda x, y: x and y, map(lambda x: e + x == x, self._elements.values())):
                    self._identity = e
                    break
        return self._identity

class Z(Group):
    def __init__(self, n):
        super(Z, self).__init__(range(n), lambda x, y : (x + y) % n)

class U(Group):
    def __init__(self, n):
        super(U, self).__init__([i for i in range(1,n) if gcd(i,n) == 1], lambda x, y : (x * y) % n)