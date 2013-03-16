from set import FiniteSet, InfiniteSet

class Integers(InfiniteSet):
    def __iter__(self):
        x = 0
        while True:
            yield x
            if x <= 0:
                x = abs(x) + 1
            else:
                x = -x
    
    def __contains__(self, x):
        return type(x) is int

class Naturals(InfiniteSet):
    def __iter__(self):
        for x in Integers():
            if x >= 0:
                yield x
    
    def __contains__(self, x):
        return x in Integers() and x >= 0

class PositiveIntegers(InfiniteSet):
    def __iter__(self):
        for x in Naturals():
            if x > 0:
                yield x
    
    def __contains__(self, x):
        return x in Integers() and x > 0

class NegativeIntegers(InfiniteSet):
    def __iter__(self):
        for x in PositiveIntegers():
            yield -x
    
    def __contains__(self, x):
        return -x in PositiveIntegers()

class Zn(FiniteSet):
    def __init__(self, n):
        super(Zn, self).__init__([i for i in range(n)])