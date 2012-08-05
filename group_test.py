import pytest
from group import Magma, Group, Z, U, DirectSum

class TestMagma:
    @classmethod
    def setup_class(self):
        self._elements = [0,1,2]
        self._magma = Magma(self._elements, lambda x, y : (x + y) % 3)
    
    def test_BadFunctionArityRaisesTypeException(self):
        with pytest.raises(TypeError):
            Magma([0,1,2,3], lambda x : x)
    
    def test_OperationNotClosedRaisesValueException(self):
        with pytest.raises(ValueError):
            Magma([0,1,2,3], lambda x, y : x + y)
    
    def test_AddValidElementsGivesAnswer(self):
        assert self._magma.add(1,2) == 0
    
    def test_AddInvalidElementsRaisesValueException(self):
        with pytest.raises(ValueError):
            self._magma.add(2, 3)
    
    def test_IteratorHitsEachElement(self):
        magmaElements = [x for x in self._magma]

class TestGroup:
    @classmethod
    def setup_class(self):
        self._elements = [0,1,2]
        self._group = Group(self._elements, lambda x, y : (x + y) % 3)
    
    def test_MissingIdentityRaisesValueException(self):
        with pytest.raises(ValueError):
            Group([1,2,3], lambda x, y : (x + y) % 3)
    
    def test_MissingInversesRaisesValueException(self):
        with pytest.raises(ValueError):
            Group([0,2], lambda x, y : (x + y) % 3)
    
    def test_InverseMaintainsIdentity(self):
        for a in self._group:
            assert self._group.add(a, self._group.invert(a)) == self._group.identity()
    
    def test_IdentityMaintainsValue(self):
        for a in self._group:
            assert self._group.add(a, self._group.identity()) == a
    
    def test_OrderGivesNumberOfElements(self):
        assert len(self._group) == len(self._elements)

class TestZ:
    @classmethod
    def setup_class(self):
        self._n = 3
        self._elements = [i for i in range(self._n)]
        self._group = Z(self._n)
    
    def test_NegativeIntegerRaisesValueException(self):
        with pytest.raises(ValueError):
            Z(-1)
    
    def test_NonIntRaisesValueException(self):
        with pytest.raises(ValueError):
            Z(1.2)
    
    def test_ElementsAreLessThanN(self):
        groupElements = [x for x in self._group]
        assert len(groupElements) == len(self._elements) and self._elements == groupElements
    
    def test_OperationIsAdditionModuloN(self):
        for a in self._elements:
            for b in self._elements:
                assert self._group.add(a, b) == (a + b) % self._n
    
    def test_StringRepresentationIsZ_n(self):
        assert str(self._group) == "Z_{0}".format(self._n)

class TestU:
    @classmethod
    def setup_class(self):
        self._n = 6
        self._elements = [1, 5]
        self._group = U(self._n)
    
    def test_NegativeIntegerRaisesValueException(self):
        with pytest.raises(ValueError):
            U(-1)
    
    def test_NonIntRaisesValueException(self):
        with pytest.raises(ValueError):
            U(1.2)
    
    def test_ElementsAreLessThanNWithGCDOne(self):
        groupElements = [x for x in self._group]
        assert len(groupElements) == len(self._elements) and self._elements == groupElements
    
    def test_OperationIsMultiplicationModuloN(self):
        for a in self._elements:
            for b in self._elements:
                assert self._group.add(a, b) == (a * b) % self._n
    
    def test_StringRepresentationIsU_n(self):
        assert str(self._group) == "U_{0}".format(self._n)

class TestDirectSum:
    @classmethod
    def setup_class(self):
        self._n1 = 5
        self._n2 = 2
        self._elements = set([(a, b) for a in range(self._n1) for b in range(self._n2)])
        self._z5Crossz2 = DirectSum(Z(self._n1), Z(self._n2))
    
    def test_ElementsAreCrossProduct(self):
        assert set([x for x in self._z5Crossz2]) == self._elements
    
    def test_IdentityIsTupleOfIdentities(self):
        e = (0, 0)
        assert self._z5Crossz2.identity() == e
    
    def test_InversesAreTupleOfInverses(self):
        inv = (3, 1)
        assert self._z5Crossz2.invert((2,1)) == inv
    
    def test_OperationIsComponentWiseOperations(self):
        x = (2, 1)
        y = (2, 1)
        z = ((x[0] + y[0]) % self._n1, (x[1] + y[1]) % self._n2)
        assert self._z5Crossz2.add(x, y) == z

class TestFactorGroup:
    @classmethod
    def setup_class(self):
        pass