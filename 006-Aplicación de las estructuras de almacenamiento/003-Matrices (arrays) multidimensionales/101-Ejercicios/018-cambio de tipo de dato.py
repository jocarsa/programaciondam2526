tupla = ('manzanas','peras','platanos')
# Necesito meter una fruta más
print(tupla)
lista = list(tupla) # convierto una tupla en una lista
print(lista)
lista.append("fresas")

# Ahora supongamos que tengo que volver a tupla
nueva_tupla = tuple(lista)
print(nueva_tupla)

