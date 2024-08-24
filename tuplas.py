#Acceder a elementos de una tupla[0]

lenguajes = ("javascript", "java", "python","java")

#print(type(lenguajes))

#print(lenguajes.count("java")) #debe ser exacta la coincidencia

#print(lenguajes[1:3])

#print(lenguajes[-1])

#print(lenguajes::2) #Esta búsqueda la haría de 2 en 2.
#print(lenguajes::5) #Esta búsqueda la haría de 3 en 3.

#print(lenguajes[-3:-1]) #Esta búsqueda inicia en reversa

# Convertir tuplas a listas.

lenguajes = ("javascript", "java", "python","go")

lenguajes = list(lenguajes)
lenguajes[1] = "JAVA"  #De manera indirecta agregamos un elemento a una tupla, pasando por una lista
lenguajes = tuple(lenguajes)
print(type(lenguajes))
print(lenguajes)

#Comprobar si un elemento está en una tupla
print("C#" in lenguajes)



#Unir tuplas
lenguaje1 = ("javascript", "java", "python","go")
lenguaje2 = ("C#",) #también se puede colocar tuple("C#")

print(type(lenguaje1))
print(type(lenguaje2))

lenguajes = lenguaje1 + lenguaje2

print(lenguajes)

del lenguajes  #esto ELIMINA la tupla llamada lenguajes
print(lenguajes) #En este caso arrojará error porque ya no existe


















