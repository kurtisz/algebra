from group.direct_sum import FiniteDirectSum as gFiniteDirectSum
from ring import FiniteRing
from operation.operation_factory import OperationFactory

class FiniteDirectSum(FiniteRing):
    '''
        Given rings R1, R2, ..., represents
        the set R1 (+) R2 (+) ...
    '''
    def __init__(self, *rings):
        self._rings = rings
        super(FiniteDirectSum, self).__init__(self.get_additive_group())
        
    def get_additive_group(self):
        return gFiniteDirectSum(*[ring.get_additive_group() for ring in self._rings])
    
    def multiply(self, x, y):
        mulXY = lambda x, y : tuple([self._rings[i].multiply(x[i], y[i]) for i in range(len(self._rings))])
        return OperationFactory.create_operation(mulXY, self).eval(x, y)
    
    def get_one(self):
        return OperationFactory.create_operation(lambda : tuple([self._rings[i].get_one() for i in range(len(self._rings))])).eval()