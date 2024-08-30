

# 1. Agrupación de objetos
#Dado una serie de productos con los siguientes parámetros:
#* Nombre (Letras y números)
#* Código de barras (sólo números)
#* Fabricante (sólo letras)
#* Categoría (sólo letras)
#* Género (Masculino o Femenino)
#Desarrollar una función que retorne un diccionario con la serie de objetos agrupados por: Fabricante → Categoría → Género

def agrupar_productos(productos):
    agrupados = {}

    for producto in productos:
        fabricante = producto['fabricante']
        categoria = producto['categoria']
        genero = producto['genero']
        
        # Verificar si el fabricante ya está en el diccionario
        if fabricante not in agrupados:
            agrupados[fabricante] = {}
        
        # Verificar si la categoría ya está en el diccionario bajo el fabricante
        if categoria not in agrupados[fabricante]:
            agrupados[fabricante][categoria] = {}
        
        # Verificar si el género ya está en el diccionario bajo la categoría
        if genero not in agrupados[fabricante][categoria]:
            agrupados[fabricante][categoria][genero] = []
        
        # Añadir el producto a la lista correspondiente
        agrupados[fabricante][categoria][genero].append(producto)
    
    return agrupados

# Ejemplo de uso con los productos dados
productos = [
    {'nombre': 'Zapatos XYZ', 'codigo_barras': '8569741233658', 'fabricante': 'Deportes XYZ', 'categoria': 'Zapatos', 'genero': 'Masculino'},
    {'nombre': 'Zapatos ABC', 'codigo_barras': '7452136985471', 'fabricante': 'Deportes XYZ', 'categoria': 'Zapatos', 'genero': 'Femenino'},
    {'nombre': 'Camisa DEF', 'codigo_barras': '5236412896324', 'fabricante': 'Deportes XYZ', 'categoria': 'Camisas', 'genero': 'Masculino'},
    {'nombre': 'Bolso KLM', 'codigo_barras': '5863219635478', 'fabricante': 'Carteras Hi-Fashion', 'categoria': 'Bolsos', 'genero': 'Femenino'},
]

resultado = agrupar_productos(productos)

from pprint import pprint
pprint(dict(resultado))
#print(resultado)

# 2. Manejo de Errores:
 #Podemos acceder a la clave del diccionario usando el metodo .get() para que el codigo sea más indulgente.
 #Al usar este método si llegamos a tener una clave inexistente Python devolvera un valor none en vez de un KeyError. 

 
diccionario = {'nombre':'Ale', 'edad': 26}
direccion = diccionario.get('direccion')
if(direccion == None):
    print ("clave inexistente en el diccionario")
else:
    print (direccion)


# 3. Supongamos que necesitas calcular el descuento aplicable en una venta según el
# total de la misma. Escribe una función en Python que tome como entrada el total de
# la venta y devuelva el porcentaje de descuento a aplicar según las siguientes reglas:
# 10% para ventas mayores a $500, 5% para ventas entre $100 y $500, y 0% para
# ventas menores a $100. 

def calcular_descuento(total_venta):
    if total_venta > 500:
        return 10  # 10% de descuento
    elif 100 <= total_venta <= 500:
        return 5  # 5% de descuento
    else:
        return 0  # 0% de descuento

# Ejemplos de uso
print(calcular_descuento(800))  # Debería devolver 10
print(calcular_descuento(250))  # Debería devolver 5
print(calcular_descuento(50))   # Debería devolver 0

# 4. Manipulación de Datos con Python:
# Supongamos que tienes una base de datos que contiene la tabla de orden de venta
# con las columnas order_id, amount_total, y customer_name. Desarrolla la query que
# permita obtener las órdenes de venta donde el amount_total es mayor a 1000.

import sqlite3
conexion = sqlite3.connect('mibasededatos.db')
cursor =conexion.cursor()

cursor.execute(""" SELECT order_id, amount_total, customer_name
FROM ordenes_venta
WHERE amount_total > 1000; """)

resultados= cursor.fetchall()
for fila in resultados: 
    print(fila)
conexion.close()

#5. Escribe una consulta SQL para encontrar los nombres de los empleados que han
# gestionado pedidos de productos de la categoría “Beverages” (Bebidas). Incluye en
# el resultado el EmployeeID, FirstName, LastName, OrderID, ProductName y
# CategoryName. Basarse en el siguiente diagrama.
# SELECT 
#     e.EmployeeID,
#     f.FirstName,
#     l.LastName,
#     o.OrderID,
#     p.ProductName,
#     c.CategoryName
# FROM 
#     Employees e
# JOIN 
#     Orders o ON e.EmployeeID = o.EmployeeID
# JOIN 
#     OrderDetails od ON o.OrderID = od.OrderID
# JOIN 
#     Products p ON od.ProductID = p.ProductID
# JOIN 
#     Categories c ON p.CategoryID = c.CategoryID
# WHERE 
#     c.CategoryName = 'Beverages';