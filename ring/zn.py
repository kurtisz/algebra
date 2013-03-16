from group.zn import Zn as gZn
from ring import FiniteRing
from operation.operation_factory import OperationFactory
from set import numeric_set

class Zn(FiniteRing, numeric_set.Zn):
    def get_additive_group(self):
        return gZn(len(self))
    
    def multiply(self, x, y):
        mulXY = lambda x, y : (x * y) % len(self)
        return OperationFactory.create_operation(mulXY, self).eval(x, y)
    
    def get_one(self):
        return OperationFactory.create_operation(lambda : 1).eval()