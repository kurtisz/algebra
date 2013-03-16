from set.direct_sum import FiniteDirectSum as sFiniteDirectSum
from group import FiniteGroup
from operation.operation_factory import OperationFactory

class FiniteDirectSum(FiniteGroup):
    '''
        Given groups G1, G2, ..., represents
        the set G1 (+) G2 (+) ...
    '''
    def __init__(self, *groups):
        super(FiniteDirectSum, self).__init__(sFiniteDirectSum(*groups))
        self._groups = groups
    
    def invert(self, x):
        invX = lambda x : tuple([self._groups[i].invert(x[i]) for i in range(len(self._groups))])
        return OperationFactory.create_operation(invX, self).eval(x)
    
    def get_identity(self):
        return OperationFactory.create_operation(lambda : tuple([self._groups[i].get_identity() for i in range(len(self._groups))])).eval()
    
    def eval(self, x, y):
        addXY = lambda x, y : tuple([self._groups[i].eval(x[i], y[i]) for i in range(len(self._groups))])
        return OperationFactory.create_operation(addXY, self).eval(x, y)