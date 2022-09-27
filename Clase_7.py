
# Las funciones son código que ya está armado para resolver algo, pero es algo suelto

# Los metodos estan relacionados a un objeto

'''METODOS PARA STRINGS'''

'''Metodo Upper:''' 

# cadena1 = 'soY la pRimer cadena'
# print(cadena1)
# cadena1_en_mayusculas = cadena1.upper()
# cadena1 = cadena1.upper()
# print(cadena1)
# print(cadena1_en_mayusculas)

'''Metodo lower:'''

# cadena1 = 'soY la pRimer cadena'
# print(cadena1)
# cadena1_en_mayusculas = cadena1.lower()
# cadena1 = cadena1.lower()
# print(cadena1)
# print(cadena1_en_mayusculas)

#Capitalize: transforma solo la primer letra en mayúscula

#title: la primer letra de cada palabra las deja en mayúscula y el retso en minúscula

#metodo count: cuenta dde el primero si no aclaro sino arranca desde donde le indico
#busca exactamente la misma letra, distingue entre mayúsculas y minus

#Metodo find: busca la cadena especificada.  si no la encuentra devuelve '-1'
#si encuentra devuelva la ubicación de la primer aparición
#también le puedo indicar desde donde a donde

#Metodo rfind: busca de derecha a izquierda

'''metodo split'''
#split devuelve una lista de cada palabra del string, cada string que separa unj espacio lo guarda como un elemento distinto en una lista
#a diferencia del list que me desagregaba un string en letras
#si() pongo un caracter, por ejemplo 'a' me va a hacer la separación cada vez que aparezca una 'a' sin tomar la 'a'
#le puedo indicar varias letras dentro del () y corta cada vez que encuentra esas letras
#siempre devuelve una lista
#si no encuentra el caracter devuelve una lista pero con el mismo string

'''metodo join:'''
#para unir, primero especifico la cadena qu quiero unir y luego a lo que lo quiero unir
#recibe solo colecciones de datos, no le puedo poner (1) por ejemplo
#es para unir en base a una palabra varias palabras


'''Metodo strip'''
#borrado de información
#elimina los espacios del ppio y del final (si no se indica nada)
#pero si le indicamos dentro del () algo saca eso que le indicamos, los elemeneot separados, no la palabra entera
#no saca la cadena tal como se la indico sino que saca los elementos que están indicados
#empieza de izq a derecha y va sacando, luego corta cuando no encuentra y empieza a barrer de derecha a izquierda hasta encontrarse con algo que no está indicado, ahi corta
#si pasamos () saca los espacios


'''replace'''
#reemplaza un string de la cadena que yo elijo por otro string, genera una nueva cadena, no reemplaza la cadena original
# si dentro de () además de las cadenas le indico un entero le estoy diciendo la cantidad de veces que quiero que se reemplace algo



'''METODOS PARA LISTAS'''

'''Metodo Clear'''
#vacía una lista
# este metodo sí modifica la lista original

'''metodo extend'''
#permite agregar, concatena
# este metodo sí modifica la lista original

'''Metodo insert'''
# nos permite agarrar un lista e insertarle un valor en una posición
# este metodo sí modifica la lista original

'''metodo reverse'''
#dar vuelta una lista

'''metodo sort'''
#ordena la lista


'''CONJUNTOS'''

'''copy'''
# genera una copia de un conjunto para poder utilizar para otras cosas

'''Metodo isdisjoint'''
#me devuelve True o False, compara dos tuplas por ej y me dice si son distintos
#se fija si todos los elementos son distintos no solo un elemento de la tupla, lista
#si hay un solo elemento igual ya me dice que es False
#el primer elemento tiene que ser un set, el segundo puede ser una lista, una tupla, otro set

'''Metodo issubset'''
#Necesitamos que el elemento base sea un set, el primer elemento sea un set, un conjunto
#COMPARA LOS VALORES DE UN SET CON los valores de un iterable (cadenas, listas, tuplas, set)
#indica si los elementos en el primer conjunto están dentro del segundo iterable


'''Metodo issuperset'''
#la inversa del issubset
#se fija si el segundo está dentro del primero

'''Metodo union'''
#devuelve un valor nuevo, devuelve un conjunto nuevo, une ambas colecciones de datos
#no modifica el conjunto base
#necesitamos que el primero sea un set, un conjunto, 


'''Metodo difference'''
#nos devuelve los datos distintos
#devuelve los valores que están dentro del primer conjunto pero que no están en el segundo iterable
#devuelve un conjunto nuevo, no modifica el base


'''Metodo difference_update'''
#permite hacer como un difference pero modifica el base
#quita del set base los elementos repetidos en el segundo

'''metodo intersection'''
#devuelve los elementos que se repiten en los dos sin modificar el conjunto base

'''metodo intersection_update'''
#modifica el base
#devuelve los elementos que se repiten modificando el conjunto base


'''DICCIONARIOS'''

'''Metodo get'''
#permite acceder a las llaves de un diccionario de forma más segura en caso de que la llave no exista
#el get le ponemos un valor por defecto por si no encuentra la llave 
#previene los errores
#no genera error sino que devuelve un valor por defecto


'''Metodo keys'''
#devuelve las llaves que tiene el diccionario
#si transfiormamos en lista el diccionario me muestra solo la lista de las llaves

'''metodo values'''
#es como el keys pero devuelve los valores de un diccionario en lugar de las llaves
#si transformamos en una lista con un list lo devuelve como una lista normal

'''metodo items'''
#permite generar una lista de tuplas que contienen llave:valor



