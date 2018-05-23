import vector # importamos las clases y metodos del archivo "vector.py"

# Creamos instancias del objeto.
# Recuerden que podemos crear el numero de instancias que querramos.
a = vector.Vector(1,2,3,4)
b = vector.Vector(5,6,7,8)
print("\n")

# Tipo de dato
print("Tipo de dato: %s" % type(a))

# Longitud del Vector
n = len(a)
print("Numero de Elementos en el vector: %s" % n)
print("\n")

# Elementos de los vectores
for x in a:
	print(x**2)
print("\n")

# Multiplicación de Vectores por escala.
mult = a * 5
print(mult)
print("\n")

# Adición de vectores
suma = a + b
print(suma)
print("\n")

# Sustracción de Vectores
res = a - b
print(res)

input()