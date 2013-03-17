from ring import FiniteRing

class FiniteRingFactory(object):
    @staticmethod
    def create_ring(add_group, mult_op):
        '''
            Return the ring defined by the
            set S over binary additive operation add_op
            and binary multiplicative operation mult_op
            
            Raises a TypeError if mult_op is not binary
            Raises a TypeError if add_group is not Abelian
            Raises a TypeError if mult_op is not associative over add_group
            Raises a TypeError if mult_op is not distributive over add_group
        '''
        if not mult_op.arity() == 2:
            raise TypeError("Ring operation must be binary")
        if not add_group.is_abelian():
            raise TypeError("Additive group must be Abelian to form a ring")
        if not FiniteRingFactory._is_associative(add_group, mult_op):
            raise TypeError("Ring operation must be associative over additive group")
        if not FiniteRingFactory._is_distributive(add_group, mult_op):
            raise TypeError("Ring operation must be distributive over additive group")
        
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
        
        return CustomRing(add_group)

    @staticmethod
    def _is_associative(add_group, mult_op):
        for x in add_group:
            for y in add_group:
                for z in add_group:
                    if not mult_op.eval(mult_op.eval(x, y), z) == mult_op.eval(x, mult_op.eval(y, z)):
                        return False
        return True
    
    @staticmethod
    def _is_distributive(add_group, mult_op):
        for x in add_group:
            for y in add_group:
                for z in add_group:
                    if not mult_op.eval(x, add_group.eval(y, z)) == add_group.eval(mult_op.eval(x, y), mult_op.eval(x, z)) or \
                       not mult_op.eval(add_group.eval(y, z), x) == add_group.eval(mult_op.eval(y, x), mult_op.eval(z, x)):
                        return False
        return True
