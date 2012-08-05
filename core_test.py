import pytest
from core import InfiniteSet, Integers, NaturalNumbers, PositiveIntegers, RealNumbers, FiniteMapping, InfiniteMapping, Operation, NullaryOperation, UnaryOperation, BinaryOperation

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

class TestIntegers:
    def test_IntegersPositiveValue(self):
        assert 5 in Integers
    
    def test_IntegersZero(self):
        assert 0 in Integers
    
    def test_IntegersNegativeValue(self):
        assert -10 in Integers
    
    def test_IntegersBadType(self):
        assert not 3.14 in Integers

class TestPositiveIntegers:
    def test_PositiveIntegersPositiveValue(self):
        assert 5 in PositiveIntegers
    
    def test_PositiveIntegersZero(self):
        assert not 0 in PositiveIntegers
    
    def test_PositiveIntegersNegativeValue(self):
        assert not -10 in PositiveIntegers
    
    def test_PositiveIntegersBadType(self):
        assert not 3.14 in PositiveIntegers

class TestNaturalNumbers:
    def test_NaturalNumbersPositiveValue(self):
        assert 5 in NaturalNumbers
    
    def test_NaturalNumbersZero(self):
        assert 0 in NaturalNumbers
    
    def test_NaturalNumbersNegativeValue(self):
        assert not -10 in NaturalNumbers
    
    def test_NaturalNumbersBadType(self):
        assert not 3.14 in NaturalNumbers

class TestRealNumbers:
    def test_RealNumbersPositiveValue(self):
        assert 5 in RealNumbers
    
    def test_RealNumbersZero(self):
        assert 0 in RealNumbers
    
    def test_RealNumbersNegativeValue(self):
        assert -10 in RealNumbers
    
    def test_RealNumbersBadType(self):
        assert 3.14 in RealNumbers
    
    def test_RealNumbersBadType(self):
        assert not "3" in RealNumbers

class TestFiniteMapping:
    @classmethod
    def setup_class(self):
        self._mapping = FiniteMapping([(3,),(4,),(5,)], lambda x : x + 3)
        
    def test_DomainElementValue(self):
        assert 7 == self._mapping.eval((4,))
    
    def test_NonDomainElementException(self):
        with pytest.raises(ValueError):
            self._mapping.eval((8,))
    
    def test_BadArityException(self):
        with pytest.raises(TypeError):
            FiniteMapping([(3,), (4,), (5,)], lambda x, y : x + y)

class TestInfiniteMapping:
    @classmethod
    def setup_class(self):
        self._mapping = InfiniteMapping(InfiniteSet(lambda x : x[0] in Integers and x[1] in Integers), lambda x, y : (x + y) % 5)
    
    def test_DomainElementValue(self):
        assert 2 == self._mapping.eval((8,9))
    
    def test_NonDomainElementException(self):
        with pytest.raises(ValueError):
            self._mapping.eval(3.14)