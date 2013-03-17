from group.zn import Zn as gZn
from ring_factory import FiniteRingFactory
from operation.operation_factory import OperationFactory

def Zn(n):
    multXY = lambda x, y : (x * y) % n
    mult_op = OperationFactory.create_operation(multXY, gZn(n))
    return FiniteRingFactory.create_ring(gZn(n), mult_op)