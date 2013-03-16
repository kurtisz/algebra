from group import FiniteGroup
from operation.operation_factory import OperationFactory
from set import numeric_set

class Zn(FiniteGroup, numeric_set.Zn):
    def invert(self, x):
        invX = lambda x : (-x) % len(self)
        return OperationFactory.create_operation(invX, self).eval(x)
    
    def get_identity(self):
        return OperationFactory.create_operation(lambda : 0).eval()
    
    def eval(self, x, y):
        addXY = lambda x, y : (x + y) % len(self)
        return OperationFactory.create_operation(addXY, self).eval(x, y)