from set.direct_sum import FiniteDirectSum as sFiniteDirectSum
from operation.operation_factory import OperationFactory
from group_factory import FiniteGroupFactory

def FiniteDirectSum(*groups):
    '''
        Given groups G1, G2, ..., represents
        the set G1 (+) G2 (+) ...
    '''
    addXY = lambda x, y : tuple([groups[i].eval(x[i], y[i]) for i in range(len(groups))])
    add_op = OperationFactory.create_operation(addXY, sFiniteDirectSum(*groups))
    return FiniteGroupFactory.create_group(add_op.get_set(), add_op)