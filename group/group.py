from set.set import FiniteSet, InfiniteSet

class Group(object):
    def invert(self, x):
        '''Return the inverse of x with respect to the group operation'''
        raise NotImplementedError("Group has not implemented inversion")
    
    def get_identity(self):
        '''Return the identity element'''
        raise NotImplementedError("Group has not implemented get_identity")
    
    def eval(self, *args):
        '''
            Evaluate the group operation on the arguments
            Raises a ValueError if x is not in the domain
        '''
        raise NotImplementedError("Group has not implemented evaluator")

class FiniteGroup(Group, FiniteSet):
    def __init__(self, S):
        super(FiniteGroup, self).__init__(S)

class InfiniteGroup(Group, InfiniteSet):
    pass