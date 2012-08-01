from fractions import gcd

class Operation(object):
    def __init__(self, domain, function):
        self._mapping = {}
        self._arity = function.func_code.co_argcount
        for x in domain:
            if len(x) != self._arity:
                raise TypeError("Function has different arity than domain element")
            self._mapping[x] = function(*x)
    
    def eval(self, x):
        if not self._mapping.has_key(x):
            raise ValueError("{0} not in domain".format(x))
        return self._mapping[x]

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