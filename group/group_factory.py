from group import FiniteGroup
from operation.operation_factory import OperationFactory

class FiniteGroupFactory(object):
    @staticmethod
    def create_group(S, op):
        '''
            Return the group defined by the
            set S over binary operation op
            
            Raises a TypeError if op is not binary
            Raises a TypeError if the group properties are not met:
                1.  Closure of op over S
                2.  Associativity of op over S
                3.  Identity element e in S (e + x = x + e = x)
                4.  Inverses -s for all s in S (s + (-s) = ((-s) + s) = e)
        '''
        if op.arity() != 2:
            raise TypeError("Group operation must be binary")
        if not FiniteGroupFactory._is_closed(S, op):
            raise TypeError("Group operation must be closed over S")
        if not FiniteGroupFactory._is_associative(S, op):
            raise TypeError("Group operation must be associative over S")
        if not FiniteGroupFactory._has_identity(S, op):
            raise TypeError("S must have an identity element for the given group operation")
        if not FiniteGroupFactory._has_inverses(S, op):
            raise TypeError("All elements of S must have inverses for the given group operation")
        
        class CustomFiniteGroup(FiniteGroup):
            def invert(self, x):
                invX = lambda x : FiniteGroupFactory._get_inverse(x, S, op)
                return OperationFactory.create_operation(invX, S).eval(x)
            
            def get_identity(self):
                iden = lambda : FiniteGroupFactory._get_identity(S, op)
                return OperationFactory.create_operation(iden).eval()
            
            def eval(self, x, y):
                return op.eval(x, y)
        
        return CustomFiniteGroup(S)
    
    @staticmethod
    def _is_closed(S, op):
        for x in S:
            for y in S:
                if not op.eval(x, y) in S:
                    return False
        return True
    
    @staticmethod
    def _is_associative(S, op):
        for x in S:
            for y in S:
                for z in S:
                    if not op.eval(op.eval(x, y), z) == op.eval(x, op.eval(y, z)):
                        return False
        return True
    
    @staticmethod
    def _has_identity(S, op):
        try:
            FiniteGroupFactory._get_identity(S, op)
            return True
        except ValueError:
            return False
    
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
    
    @staticmethod
    def _get_identity(S, op):
        for e in S:
            found_identity = True
            for x in S:
                if not op.eval(e, x) == op.eval(x, e) or not op.eval(e, x) == x:
                    found_identity = False
                    break
            if found_identity:
                return e
        raise ValueError("Could not find identity for set")
    
    @staticmethod
    def _get_inverse(x, S, op):
        e = FiniteGroupFactory._get_identity(S, op)
        for y in S:
            if op.eval(x, y) == op.eval(y, x) and op.eval(x, y) == e:
                return y
        raise ValueError("Could not find inverse for given element")