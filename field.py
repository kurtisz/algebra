from ring import Ring

class Field(object):
    def __init__(self, group, function):
        self._additiveGroup = group
        self._multiplicativeGroup = Group([x for x in self._additiveGroup], function)
    
    def add(self, a, b):
        return self._additiveGroup.add(a, b)
    
    def multiply(self, a, b):
        return self._multiplicativeGroup.add(a, b)
    
    def negate(self, a):
        return self._additiveGroup.invert(a)
    
    def invert(self, a):
        return self._multiplicativeGroup.invert(a)
    
    def __iter__(self):
        for a in self._additiveGroup:
            yield a
    
    def __len__(self):
        return len(self._additiveGroup)