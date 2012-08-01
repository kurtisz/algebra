import pytest
from core import Operation, NullaryOperation, UnaryOperation, BinaryOperation

class TestOperation:
    @classmethod
    def setup_class(self):
        self._operation = Operation([(1,2,3), (2,1,3), (2,3,1)], lambda x, y, z : x + y * z)
    
    def test_EvaluationOfDomainElement(self):
        assert self._operation.eval((1,2,3)) == 7
    
    def test_EvaluationOfNonDomainElementRaisesValueError(self):
        with pytest.raises(ValueError):
            self._operation.eval((3,2,1))
    
    def test_BadArityRaisesTypeException(self):
        with pytest.raises(TypeError):
            Operation([(3,2), (1,2), (3,1), (1,1)], lambda x : x)

class TestNullaryOperation:
    @classmethod
    def setup_class(self):
        self._operation = NullaryOperation(3)
    
    def test_EvaluationGivesValue(self):
        assert self._operation.eval() == 3

class TestUnaryOperation:
    @classmethod
    def setup_class(self):
        self._operation = UnaryOperation([1,2,3,4], lambda x : 3 * x)
        
    def test_EvaluationOfDomainElementGivesValue(self):
        assert self._operation.eval(4) == 12
        
    def test_BadArityRaisesTypeException(self):
        with pytest.raises(TypeError):
            UnaryOperation([1,2,3], lambda x, y : x + y)

class TestBinaryOperation:
    @classmethod
    def setup_class(self):
        self._operation = BinaryOperation([0,1,2,3,4], lambda x, y : (x * y) % 5)
    
    def test_EvaluationOfDomainElementGivesValue(self):
        assert self._operation.eval(3, 4) == 2
    
    def test_BadArityRaisesTypeException(self):
        with pytest.raises(TypeError):
            BinaryOperation([1,2,3,4], lambda x : x)