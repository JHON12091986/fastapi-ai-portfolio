def calculate_discount(price, discount_percentage):
    """
    Calcula el precio final después de aplicar un descuento.
    Ejemplo: price=100, discount=20 -> retorna 80.0
    """
    # Si el descuento es mayor a 100, lanzamos un error
    if discount_percentage > 100:
        raise ValueError("El descuento no puede ser mayor a 100%")
        
    # Corregimos el cálculo: dividimos el porcentaje entre 100
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount