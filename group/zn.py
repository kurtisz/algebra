from group import FiniteGroup
from operation.operation import NullaryOperation, UnaryOperation, BinaryOperation
from set import numeric_set

class Zn(FiniteGroup, numeric_set.Zn):
    class ModularInversion(UnaryOperation):
        def __init__(self, S):
            self._set = S
            self._n = len(self._set)
        
        def eval(self, *args):
            x = self.get_arguments(*args)[0]
            return (-x) % self._n
        
        def get_set(self):
            return self._set
    
    class ModularAddition(BinaryOperation):
        def __init__(self, S):
            self._set = S
            self._n = len(S)
            
        def eval(self, *args):
            x, y = self.get_arguments(*args)
            return (x + y) % self._n
    
        def get_set(self):
            return self._set
    
    def invert(self, x):
        return Zn.ModularInversion(self).eval(x)
    
    def get_identity(self):
        return NullaryOperation(0).eval()
    
    def eval(self, x, y):
        return Zn.ModularAddition(self).eval(x, y)