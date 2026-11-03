import pytest
from buggy_checkout import calculate_discount

def test_normal_discount():
    # Si algo cuesta 100 y hay 20% de descuento, debería costar 80
    assert calculate_discount(100, 20) == 80.0

def test_invalid_discount():
    # Si el descuento es mayor a 100, debería fallar
    with pytest.raises(ValueError):
        calculate_discount(100, 150)