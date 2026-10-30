import pytest
from inventory import calculate_total_price

def test_calculate_total_price_with_valid_products():
    products = [
        {"name": "Laptop", "price": 1000.0},
        {"name": "Mouse", "price": 25.50}
    ]
    assert calculate_total_price(products) == 1025.50

def test_calculate_total_price_with_empty_list():
    assert calculate_total_price([]) == 0.0

def test_calculate_total_price_ignores_invalid_prices():
    products = [
        {"name": "Laptop", "price": 1000.0},
        {"name": "Freebie", "price": 0},
        {"name": "Broken", "price": -50},
        {"name": "No price key"}, # Sin la llave price
        {"name": "String price", "price": "100"} # Precio como string
    ]
    # Solo debería sumar el precio de la Laptop (1000.0)
    assert calculate_total_price(products) == 1000.0