from ring import FiniteRing
from group.group_factory import FiniteGroupFactory
from operation.operation_factory import OperationFactory

class FiniteRingFactory(object):
    @staticmethod
    def create_ring(S, add_op, mult_op):
        '''
            Return the ring defined by the
            set S over binary additive operation add_op
            and binary multiplicative operation mult_op
            
            Raises a TypeError if (S, add_op) is not a group
            Raises a TypeError if (S \ {0}, mult_op) is not a group
        '''
        add_group = FiniteGroupFactory.create_group(S, add_op)
        mult_group = FiniteGroupFactory.create_group(S.remove(add_group.get_identity()), mult_op)
        
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
        
        return CustomRing(S)