def calculate_total_price(products):
    """
    Recibe una lista de diccionarios de productos (ej. [{"name": "Laptop", "price": 1000}])
    y devuelve el precio total.
    Ignora los productos que no tengan precio o cuyo precio sea menor a cero.
    """
    if not products:
        return 0.0
    
    total = 0.0
    for product in products:
        # Usamos .get() para evitar errores si la llave 'price' no existe
        price = product.get("price")
        if isinstance(price, (int, float)) and price > 0:
            total += price
            
    return total