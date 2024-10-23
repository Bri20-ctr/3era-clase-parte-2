
# Práctica Listas 1
mi_lista = [42, "Hola", True, 3.14, "Python"]

# Práctica Listas 2
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

# Práctica Listas 3
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)

#-------------------------------------------------------------------

mi_diccionario = {
    "curso": "Python TOTAL",
    "clase": "Diccionarios"
}
mi_diccionario["recursos"] = ["notas", "ejercicios"]

print(mi_diccionario.keys())
print(mi_diccionario.values())
print(mi_diccionario.items())

# Práctica Diccionarios 1
mi_dic = {
    "nombre": "Karen",
    "apellido": "Jurgens",
    "edad": 35,
    "ocupacion": "Periodista"
}

# Práctica Diccionarios 2
mi_dict = {
    "valores_1": {"v1": 3, "v2": 6},
    "puntos": {"points1": 9, "points2": [10, 300, 15]}
}
print(mi_dict["puntos"]["points2"][1])

# Práctica Diccionarios 3
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"

#---------------------------------------------------------------------

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)

mi_tuple = (1, "dos", [3.33, "cuatro"], (5.0, 6))

lista_1 = list(mi_tuple)
print(lista_1)

a, b, c, d = mi_tuple
print(c)

# Práctica Tuples 1
veces_2 = mi_tupla.count(2)
print(veces_2)

# Práctica Tuples 2
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

# Práctica Tuples 3
mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla
