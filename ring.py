import magma, group

class Ring(object):
    def __init__(self, group, function):
        self._group = group
        self._magma = Magma([x for x in self._group], function)
    
    def add(self, a, b):
        return self._group.add(a, b)
    
    def multiply(self, a, b):
        return self._magma.add(a, b)
    
    def negate(self, a):
        return self._group.invert(a)
    
    def __iter__(self):
        for a in self._group:
            yield a
    
    def __len__(self):
        return len(self._group)

class Z(Ring):
    def __init__(self, n):
        super(Z, self).__init__(group.Z(n), lambda x, y : (x * y) % n)
    
    def __str__(self):
        return "Z_{0}".format(len(self))

class DirectSum(Ring):
    def __init__(self, *rings):
        self._rings = rings
        group = group.DirectSum(rings)
        function = lambda x, y : tuple([rings[i].multiply(x[i], y[i]) for i in range(len(rings))])
        super(DirectSum, self).__init__(group, function)
    
    def __str__(self):
        s = str(self._groups[0])
        for R in self._rings[1:]:
            s += " + " + str(R)
        return s