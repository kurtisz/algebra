from operation.operation_factory import OperationFactory
from group_factory import FiniteGroupFactory
from set import numeric_set

def Zn(n):
    '''
        Group of integers under addition modulo n
    '''
    addXY = lambda x, y : (x + y) % n
    add_op = OperationFactory.create_operation(addXY, numeric_set.Zn(n))
    return FiniteGroupFactory.create_group(add_op.get_set(), add_op)