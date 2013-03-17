from ring import FiniteRing
from group.group_factory import FiniteGroupFactory
from operation.operation_factory import OperationFactory

class FiniteRingFactory(object):
    @staticmethod
    def create_ring(add_group, mult_op):
        '''
            Return the ring defined by the
            set S over binary additive operation add_op
            and binary multiplicative operation mult_op
            
            Raises a TypeError if (S, add_op) is not a group
            Raises a TypeError if (S \ {0}, mult_op) is not a group
        '''
        zero = add_group.get_identity()
        mult_group = FiniteGroupFactory.create_group(add_group.remove(zero), mult_op)
        
        class CustomRing(FiniteRing):
            def get_additive_group(self):
                return add_group
            
            def add(self, x, y):
                return add_group.eval(x, y)
            
            def negate(self, x):
                return add_group.invert(x)
            
            def get_zero(self):
                return add_group.get_identity()
            
            def multiply(self, x, y):
                return mult_op.eval(x, y)
            
            def get_one(self):
                return mult_group.get_identity()
        
        return CustomRing(add_group)

    @staticmethod
    def _has_inverses(S, op):
        for x in S:
            if not FiniteGroupFactory._has_inverse(x, S, op):
                return False
        return True
    
    @staticmethod
    def _has_inverse(x, S, op):
        try:
            FiniteGroupFactory._get_inverse(x, S, op)
            return True
        except ValueError:
            return False