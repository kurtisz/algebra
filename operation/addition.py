from operation import BinaryOperation

class Addition(BinaryOperation):
    def __init__(self, S):
        self._set = S
        
    def eval(self, *args):
        if len(args) != 2:
            raise ValueError("Too few arguments supplied to binary operator")
        x, y = args[0], args[1]
        if not ((x in self._set) and (y in self._set)):
            raise ValueError("Arguments to operation (" + str(x) + ", " + str(y) + ") not members of the domain")
        return x + y
    
    def get_set(self):
        return self._set