from group import FiniteGroup
from operation.operation_factory import OperationFactory

class FiniteDirectSum(FiniteGroup):
    def __init__(self, *groups):
        if len(groups) < 2:
            raise ValueError("Direct sum must be composed of at least two groups")
        elements = [[]]
        for group in groups:
            new_elements = []
            for x in group:
                new_elements += [e + [x] for e in elements]
            elements = new_elements
        elements = map(lambda e : tuple(e), elements)
        super(FiniteDirectSum, self).__init__(elements)
        self._groups = groups
    
    def invert(self, x):
        invX = lambda x : tuple([self._groups[i].invert(x[i]) for i in range(len(self._groups))])
        return OperationFactory.create_operation(1, invX, self).eval(x)
    
    def get_identity(self):
        return OperationFactory.create_operation(0, lambda : tuple([self._groups[i].get_identity() for i in range(len(self._groups))])).eval()
    
    def eval(self, x, y):
        addXY = lambda x, y : tuple([self._groups[i].eval(x[i], y[i]) for i in range(len(self._groups))])
        return OperationFactory.create_operation(2, addXY, self).eval(x, y)