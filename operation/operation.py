class Operation(object):
    def eval(self, *args):
        '''
            Evaluate the operation on the arguments
            Raises a ValueError if x is not in the domain
        '''
        raise NotImplementedError("Operation has not implemented evaluator")
    
    def arity(self):
        '''Return the number of arguments accepted by the operation'''
    
    def get_set(self):
        '''Return the set over which the operation is defined'''
    
    def get_arguments(self, *args):
        '''
            Validates the number and type of arguments received
            Raises a ValueError if the number of arguments does not match arity
            Raises a ValueError if any one of the arguments is not in the domain
        '''
        if len(args) != self.arity():
            raise ValueError("Incorrect number of arguments supplied to operator")
        argument_membership = [x in self.get_set() for x in args]
        if False in argument_membership:
            raise ValueError("Arguments to operation " + str(args[argument_membership.index(False)]) + " not a member of the domain")
        return args

class NullaryOperation(Operation):
    def __init__(self, value):
        self._value = value
    
    def eval(self, *args):
        self.get_arguments(*args)
        return self._value
    
    def arity(self):
        return 0
    
    def get_set(self):
        return set()

class UnaryOperation(Operation):
    def arity(self):
        return 1

class BinaryOperation(Operation):
    def arity(self):
        return 2