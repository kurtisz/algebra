from set.set import FiniteSet, InfiniteSet

class Ring(object):
    def get_additive_group(self):
        '''Return the additive subgroup'''
        raise NotImplementedError("Ring has not implemented get_additive_group")
    
    def add(self, x, y):
        '''
            Evaluate the group operation on the arguments
            Raises a ValueError if x, y not in the domain
        '''
        return self.get_additive_group().eval(x, y)
    
    def negate(self, x):
        '''Return the additive inverse of x'''
        return self.get_additive_group().invert(x)
    
    def get_zero(self):
        '''Return the additive identity element'''
        return self.get_additive_group().get_identity()
    
    def multiply(self, x, y):
        '''
            Evaluate the ring operation on the arguments
            Raises a ValueError if x, y not in the domain
        '''
        raise NotImplementedError("Ring has not implemented evaluator")

class FiniteRing(Ring, FiniteSet):
    def __init__(self, S):
        super(FiniteRing, self).__init__(S)

class InfiniteRing(Ring, InfiniteSet):
    pass