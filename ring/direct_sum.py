from group.direct_sum import FiniteDirectSum as gFiniteDirectSum
from ring_factory import FiniteRingFactory
from operation.operation_factory import OperationFactory

def FiniteDirectSum(*rings):
    '''
        Given rings R1, R2, ..., represents
        the set R1 (+) R2 (+) ...
    '''
    mulXY = lambda x, y : tuple([rings[i].multiply(x[i], y[i]) for i in range(len(rings))])
    add_group = gFiniteDirectSum(*[ring.get_additive_group() for ring in rings])
    print add_group
    print add_group.remove(add_group.get_identity())
    mult_op = OperationFactory.create_operation(mulXY, add_group)
    return FiniteRingFactory.create_ring(add_group, mult_op)