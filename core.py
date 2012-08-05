from fractions import gcd

Infinity = float("inf")

class InfiniteSet(object):
    def __init__(self, contains):
        if not contains.func_code.co_argcount == 1:
            raise TypeError("Contains function must accept one argument")
        self._contains = contains
    
    def __contains__(self, x):
        try:
            return self._contains(x)
        except:
            return False
    
    def __len__(self):
        return Infinity

Integers = InfiniteSet(lambda x : type(x) == int)
PositiveIntegers = InfiniteSet(lambda x : x in Integers and x > 0)
NaturalNumbers = InfiniteSet(lambda x : x in Integers and x >= 0)
RealNumbers = InfiniteSet(lambda x : x in Integers or type(x) == float)

class FiniteMapping(object):
    def __init__(self, domain, function):
        for x in domain:
            if len(x) != function.func_code.co_argcount:
                raise TypeError("Function has different arity than domain element")
        self._domain = domain
        self._function = function
    
    def eval(self, x):
        if x in self._domain:
            return self._function(*x)
        else:
            raise ValueError("{0} not in domain".format(x))
    
    def __eq__(self, other):
        return self._mapping == other._mapping

class InfiniteMapping(object):
    def __init__(self, domain, function):
        self._domain = domain
        self._function = function
    
    def eval(self, x):
        if not x in self._domain:
            raise ValueError("{0} not in domain".format(x))
        return self._function(*tuple(x))
    
    def __eq__(self, other):
        return False

class Operation(object):
    def __init__(self, domain, function):
        if len(domain) < Infinity:
            self._mapping = FiniteMapping(domain, function)
        else:
            self._mapping = InfiniteMapping(domain, function)
    
    def eval(self, x):
        return self._mapping.eval(x)
    
    def __eq__(self, other):
        return self._mapping == other._mapping

class NullaryOperation(Operation):
    def __init__(self, value):
        super(NullaryOperation, self).__init__([()], lambda : value)
    
    def eval(self):
        return super(NullaryOperation, self).eval(())

class UnaryOperation(Operation):
    def __init__(self, domain, function):
        if function.func_code.co_argcount != 1:
            raise TypeError("Given function is not unary")
        super(UnaryOperation, self).__init__([(x,) for x in domain], function)
    
    def eval(self, x):
        return super(UnaryOperation, self).eval((x,))

class BinaryOperation(Operation):
    def __init__(self, domainSet, function):
        if function.func_code.co_argcount != 2:
            raise TypeError("Given function is not binary")
        super(BinaryOperation, self).__init__([(x,y) for x in domainSet for y in domainSet], function)
    
    def eval(self, x, y):
        return super(BinaryOperation, self).eval((x,y,))