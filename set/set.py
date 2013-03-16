class Set(object):
    def __iter__(self):
        '''Allows for iteration over the set elements'''
        raise NotImplementedError("Set has not implemented iterator")
    
    def __contains__(self, x):
        '''Checks for set membership'''
        raise NotImplementedError("Set has not implemented membership check")
    
    def __len__(self):
        '''Returns the size of the set'''
        raise NotImplementedError("Set has not implemented length method")

class FiniteSet(Set):
    def __init__(self, elements):
        self._elements = elements
    
    def __iter__(self):
        for x in self._elements:
            yield x
    
    def __contains__(self, x):
        return x in self._elements
    
    def __len__(self):
        return len(self._elements)
    
    def __str__(self):
        return '{' + str(self._elements)[1:-1] + '}'
    
    def remove(self, x):
        return FiniteSet([e for e in self._elements if not e == x])

class InfiniteSet(Set):
    def __len__(self):
        return float('inf')