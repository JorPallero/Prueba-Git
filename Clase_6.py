# lista = ['soy', 'una', 'lista', 2, True]
# tupla = ('soy', 'una', 'lista', 2, True)
# conjunto = {'soy', 'una', 'lista', 1, True}

# print (lista[1])
# print (tupla[1])
# print (conjunto [1])

# # listas se pueden modificar, las tuplas no se pueden modificar
# # Un set no tiene índice

# #como no tiene índice no me muestra los elementos en orden

# #aunque no maneje un índice interno lo que hace es decir acá se guarda el conjunto, entonces esto se va a guardar con una posición interna para la pc

# #un conjunto no mantiene duplicacion de valores

# #si en un conjunto pongo un 1 y un True, el True lo toma como un 1 y lo toma como duplicado, no lo muestra

# # print(conjunto)

# #las tuplas están optimizadas para busquedas, un set está optimizado para funcionalidades a los teoremos de conjuntos que se trabajan en matemáticas

# #las tuplas son inmutables, las listas sí, los sets necesitan que los valores guardados sean inmutables
# #por eso si guardo una lista dentro de una tupla no se puede, da error


# #con una colección podemos castear a un set, pero si tiene una lista dentro da error
# #podemos trasformar tuplas y listas a un set

# # podemos transformar, castear un range a un set

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print (auto)

# #para agregarle elementos al set es add:

# auto.add ('descapotable')
# print(auto)

# lista = [1, 2, 3, 'probando']
# auto.add (lista) #da error porque no se pueden poner listas porque se pueden modificfar

# print(auto)

#con add puedo agregar un elemento a la vez, si agrego una tupla entera ,me la toma como un solo elemento

#update agarra una colección de datos y la guarda, mete cada elemento de la lista y los guarda por separado

# auto.update (lista)

# print(auto)

#con update agrego los valores dentro, con add agrega la lista, tupla como si fuera un solo elemento

#si hago un update con una cadena, por ejemplo 'hola', agrega cada letra por separado

#con range el update funciona igual, agrega cada elemento por separado

#discard nos permite poder eliminar elementos

#si queremos eliminar algo que no está en la lista no pasa nada, no da error

#remove si genera error, si no se encuentra el elemento que quiero eliminar da error

#si queremos saber si el elemento está o no nos conviene utilizar un remove, sino un discard

#Operador IN, nos sirve para poder saber si un eleemnto está dentro de un set, lista, tupla, etc

#IN y NOT IN, generan booleanos

#CLEAR permite limpiar un conjunto, lo vaciamos

#POP elimina un elemento de una lista, si no indicamos el índice sacaba el último

#en el set saca elemento tras elemento, no saca el último porque en un conjunto no hay orden

#pop en un set no puede indicarse índice prque un set no tiene índices



#DICCIONARIOS

dicc = {}

#el dicc guarda los valores usando una llave, clave, key
#la key debe ser un valor inmutable
#los valores pueden ser de cualquier tipo

#el valor asignado a una clave puede ser otro diccionario

# una key puede ser una tupla porque no se pueden modificar"

# auto = {
#     'motor':'v8',
#     'color':'negro',
#     'vidrios':(6, 'blindadas')
# }

# print(auto)

#para diccionarios no usamos los pindices sino que accedemos a los elementos con los [] y pasandole la clave

#si pongo una clave que no existe nme da error

#si pongo get: auto.get('motor'), me devuelve el valor de esa clave

#si pongo get y agrego una cleve que no existe no me genera error sino que me devuelve 'none'

#none es un tipo de dato que devuelve la nada misma, no es un error, no es falso

#get me permite definir qué valor puedo utilizar si no existe esa clave


#FUNCIONES DICCIONARIOS

#len (CUANTOS CLAVES Y VALORES HAY en conjunto)
#update (modificar varios elementos).  Permite 2 formas de guardado
#update, las clave valor que ya están las actualiza y las que no están las agrega
#update, en lugar de usar un diccionario, usamos una tupla entera que tenga tuplas dentro que sean llave:valor

#IN , no busca que se encuentreel valor dentro del diccionario

#del borra llaves dentro de un diccionario. si queremos borrar algo que no se encuentra genera error

#clear, borra todo lo que está dentro del diccionario

#Pop nos pide si o si que le indiquemos la llave a borrar sino da error

#pop nos borra la llave:valor pero nos permite guardar el valor si lo guardamos en una variable por ejemplo

#si no existe la llave que quiero borrar genera un error

#pop nps permite hacer como el get, nos permite pasarle un valor en caso de que no se encuentre la llave indicada



