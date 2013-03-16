from operation import Operation

class OperationFactory(object):
    @staticmethod
    def create_operation(func, S=set()):
        '''
            Returns the operation defined
            by the set over the function
        '''
        arity = func.func_code.co_argcount
        class CustomOperation(Operation):
            def eval(self, *args):
                args = self.get_arguments(*args)
                return func(*args)
            
            def get_set(self):
                return S
            
            def arity(self):
                return arity
        
        return CustomOperation()