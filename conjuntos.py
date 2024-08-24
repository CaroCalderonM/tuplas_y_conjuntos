# Es una colección de elementos distintos no ordenados y NO indexados
#sets

#syntax / sin
st = set()
fruits = {'banana', 'orange', 'mango', 'lemon'}

conjunto = set({1,2,3,4,5})  #este es un conjunto o set

print(type(conjunto))

print(len(conjunto))


#comprobar si un elemento está en un set
print(3 in conjunto)

#Agregar elementos en un set ->add
conjunto = set({1,2,3,4,5})

conjunto.add(6)
print(conjunto)

#Eliminar elementos -> remove
conjunto.remove(2)
print(conjunto)

conjunto = set({1,2,3,4,5})
conjunto.remove(10) # Ene este caso nos dará error porque 10 no existe en este conjunto
print(conjunto)

# Agregar varios elementos -> update()

conjunto = set({1,2,3,4,5})
conjunto.update([6,7,8,9])
conjunto.update([2,7,9,])  #No agrega el dato si es que el conjunto YA tiene ese elemento
print(conjunto)

#Remover de forma aleatoria -> pop

conjunto = set({1,2,3,4,5})
conjunto.pop()  #Elimina un elemento aleatoriamente
print(conjunto)

#si queremos eliminar un elemento especícifo, usamos remove


#Limpiar o vaciar un conjunto -> clear
conjunto = set({1,2,3,4,5})
conjunto.clear()
print(conjunto)


#Unir conjuntos -> union()

conjunto1 = set({1,2,3,4,5})
conjunto2 = set({1,2,8,9,10})
conjunto1.union(conjunto2)  #En este caso NO lo agrega.

conjuntos = conjunto1.union(conjunto2)

print(conjunto1)

#Intersección de elementos
conjunto1 = set({1, 5, 7, 2})
conjunto2 = set({2, 5, 9})

interseccion = conjunto1.intersection(conjunto2)

print(interseccion)

# diferencias
conjunto1 = set({1, 5, 7, 2})
conjunto2 = set({2, 5, 9})

diferentes = conjunto1.difference(conjunto2) #Muestra los que del conjunto1 No están en el 2
print(diferentes) 

diferentes = conjunto2.difference(conjunto1) #Muestra los que del conjunto2 No están en el 1
print(diferentes)

#Hacer ejercicio de unir 2 conjuntos y luego ver si Issuperset() de la intersección de esos mismos conjuntos






















