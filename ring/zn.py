from group.zn import Zn as gZn
from ring import FiniteRing
from operation.operation import NullaryOperation, BinaryOperation
from set import numeric_set

class Zn(FiniteRing, numeric_set.Zn):
    class ModularMultiplication(BinaryOperation):
        def __init__(self, S):
            self._set = S
            self._n = len(S)
            
        def eval(self, *args):
            x, y = self.get_arguments(*args)
            return (x * y) % self._n
    
        def get_set(self):
            return self._set
    
    def get_additive_group(self):
        return gZn(len(self))
    
    def multiply(self, x, y):
        return Zn.ModularMultiplication(self).eval(x, y)
    
    def get_one(self):
        return NullaryOperation(1).eval()