from set.set import FiniteSet, InfiniteSet

class Group(object):
    def invert(self, x):
        '''Return the inverse of x with respect to the group operation'''
        raise NotImplementedError("Group has not implemented inversion")
    
    def get_identity(self):
        '''Return the identity element'''
        raise NotImplementedError("Group has not implemented get_identity")
    
    def eval(self, x, y):
        '''
            Evaluate the group operation on the arguments
            Raises a ValueError if x, y not in the domain
        '''
        raise NotImplementedError("Group has not implemented evaluator")
    
    def is_abelian(self):
        '''
            Is the group Abelian (commutative)
        '''
        return False

class FiniteGroup(Group, FiniteSet):
    def __init__(self, S):
        super(FiniteGroup, self).__init__(S)

class FiniteAbelianGroup(FiniteGroup):
    def is_abelian(self):
        return True

class InfiniteGroup(Group, InfiniteSet):
    pass