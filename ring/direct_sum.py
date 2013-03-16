from group.direct_sum import FiniteDirectSum as gFiniteDirectSum
from ring import FiniteRing
from operation.operation import NullaryOperation, BinaryOperation

class FiniteDirectSum(FiniteRing):
    class ElementwiseMultiplication(BinaryOperation):
        def __init__(self, S, *rings):
            self._set = S
            self._rings = rings
            
        def eval(self, *args):
            x, y = self.get_arguments(*args)
            return tuple([self._rings[i].multiply(x[i], y[i]) for i in range(len(self._rings))])
    
        def get_set(self):
            return self._set
        
    def __init__(self, *rings):
        self._rings = rings
        super(FiniteDirectSum, self).__init__([e for e in self.get_additive_group()])
        
    def get_additive_group(self):
        return gFiniteDirectSum(*[ring.get_additive_group() for ring in self._rings])
    
    def multiply(self, x, y):
        return FiniteDirectSum.ElementwiseMultiplication(self, *self._rings).eval(x, y)
    
    def get_one(self):
        return NullaryOperation(tuple([self._rings[i].get_one() for i in range(len(self._rings))])).eval()