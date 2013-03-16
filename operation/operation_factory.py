from operation import Operation

class OperationFactory(object):
    @staticmethod
    def create_operation(arity, func, S=set()):
        class CustomOperation(Operation):
            def eval(self, *args):
                args = self.get_arguments(*args)
                return func(*args)
            
            def get_set(self):
                return S
            
            def arity(self):
                return arity
        
        return CustomOperation()