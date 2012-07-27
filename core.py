from fractions import gcd
from groupUtils import getInverse

class Atom(object):
    def __init__(self, value):
        self._value = value
    
    def __str__(self):
        return str(self._value)
    
    def eval(self):
        return self._value
    
    def __hash__(self):
        return hash(self._value)
    
    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        return self._value == other._value

class Set(object):
    def __init__(self, atoms):
        self._elements = []
        for a in atoms:
            if not a in self._elements:
                self._elements.append(a)
    
    def __contains__(self, atom):
        return atom in self._elements
    
    def __iter__(self):
        for a in self._elements:
            yield a
    
    def __len__(self):
        return len(self._elements)
    
    def __eq__(self, other):
        if not type(other) == type(self):
            return False
        if not len(self) == len(other):
            return False
        for a in self._elements:
            if not a in other:
                return False
        return True
    
    def __str__(self):
        return str([str(a) for a in self._elements])

class Operation(object):
    '''
        Represents an n-ary operation
        for a given domain
        
        Domains must be sets of n-tuples
        for the given n-ary operation
    '''
    
    def __init__(self, domain, function):
        self._domain = domain
        self._arity =function.func_code.co_argcount
        self._mapping = {x:applyFunction(function, x) for x in domain}
    
    def eval(self, x):
        if x not in self._domain:
            raise ValueError("{0} not in domain".format(x))
        return self._mapping[x]
    
    def arity(self):
        return self._arity
    
    def __len__(self):
        return self.arity()

class NullaryOperation(Operation):
    def __init__(self, value):
        super(NullaryOperation, self).__init__([()], lambda : value)
    
    def eval(self):
        return super(NullaryOperation, self).eval(())

class BinaryOperation(Operation):
    def __init__(self, S, function):
        super(BinaryOperation, self).__init__(reduce(lambda row1, row2: row1 + row2, [[(a, b) for b in S] for a in S]), function)

def applyFunction(f, tup):
    if type(tup) == type(1):
        return f(tup)
    if type(tup) == Atom:
        return f(tup.eval())
    if len(tup) == 0:
        return f()
    return f(*map(lambda x : x.eval(), tup))

class Magma(object):
    '''
        A set closed over a binary operation
    '''
    
    def __init__(self, elements, function):
        self._set = Set(elements)
        self._operation = BinaryOperation(self._set, function)
    
    def add(self, a, b):
        if (not a in self._set) or (not b in self._set):
            raise ValueError("({0}, {1}) not in domain".format(a, b))
        return self._operation.eval((a,b))
    
    def __iter__(self):
        for a in self._set:
            yield a