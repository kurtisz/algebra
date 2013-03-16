from set import FiniteSet

class FiniteDirectSum(FiniteSet):
    '''
        Given sets S1, S2, ..., represents
        the set S1 (+) S2 (+) ...
    '''
    def __init__(self, *sets):
        if len(sets) < 2:
            raise ValueError("Direct sum must be composed of at least two sets")
        elements = [[]]
        for S in sets:
            new_elements = []
            for x in S:
                new_elements += [e + [x] for e in elements]
            elements = new_elements
        elements = map(lambda e : tuple(e), elements)
        super(FiniteDirectSum, self).__init__(elements)