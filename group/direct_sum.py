from group import FiniteGroup
from operation.operation import NullaryOperation, UnaryOperation, BinaryOperation

class FiniteDirectSum(FiniteGroup):
    class ElementwiseInversion(UnaryOperation):
        def __init__(self, S, *groups):
            self._set = S
            self._groups = groups
        
        def eval(self, *args):
            x = self.get_arguments(args)[0]
            return tuple([self._groups[i].invert(x[i]) for i in range(len(self._groups))])
        
        def get_set(self):
            return self._set
        
    class ElementwiseOperation(BinaryOperation):
        def __init__(self, S, *groups):
            self._set = S
            self._groups = groups
            
        def eval(self, *args):
            x, y = self.get_arguments(*args)
            return tuple([self._groups[i].eval(x[i], y[i]) for i in range(len(self._groups))])
    
        def get_set(self):
            return self._set
        
    def __init__(self, *groups):
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
        return FiniteDirectSum.ElementwiseInversion(self, *self._groups).eval(*x)
    
    def get_identity(self):
        return NullaryOperation(tuple([self._groups[i].get_identity() for i in range(len(self._groups))])).eval()
    
    def eval(self, *args):
        return FiniteDirectSum.ElementwiseOperation(self, *self._groups).eval(*args)