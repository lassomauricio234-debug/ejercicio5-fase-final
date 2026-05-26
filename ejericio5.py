# ==============================
# Sistema de Promoción Restaurante
# ==============================

# Matriz del menú
# [Nombre, Categoría, Precio Base]

menu = [
    ["Hamburguesa", "Comida Rapida", 25000],
    ["Pizza", "Comida Rapida", 35000],
    ["Ensalada", "Saludable", 18000],
    ["Pasta", "Italiana", 42000],
    ["Sushi", "Japonesa", 50000],
    ["Tacos", "Mexicana", 28000]
]

# Variables de la promoción
categoria_objetivo = "Comida Rapida"
umbral_precio = 30000
descuento = 0.15


# Función para calcular precio final
def calcular_precio_final(categoria, precio):
    
    # Verificar condiciones
    if categoria == categoria_objetivo and precio > umbral_precio:
        precio_final = precio - (precio * descuento)
    else:
        precio_final = precio

    return precio_final


# Mostrar resultados
print("===== MENÚ DEL RESTAURANTE =====\n")

for producto in menu:
    
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Calcular precio final
    precio_final = calcular_precio_final(categoria, precio_base)

    # Mostrar información
    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)
    print("Precio Final: $", precio_final)
    print("-----------------------------")
    
    