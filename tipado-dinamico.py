# variables x e y apuntan al objeto "8".
x = 8
y = x
print(x)
print(y)

# Se cambia el objeto al que apunta x.
x = 'test'
print(x)
print(y)

#Las listas lista_1 y lista_2 apuntan al mismo objeto.
lista_1 = [9, 8, 7]
lista_2 = lista_1
print(lista_1)
print(lista_2)

# Se modifica un elemento del objeto, más no se modifica el objeto.
lista_1[2] = 5
print(lista_1)
print(lista_2)
# Por lo tanto ambas listas se verán afectadas por la modificación.

# Si se requiere comprobar el tipo de una variable se hace uso de la función "type()"
z = 35
print(type(z))
z = "ahora es una cadena de texto"
print(type(z))
