
#podemos tener en lugar de un return con valores, un return que no haga nada


# serviría para cortar la ejecución, serviría como un break

#cuando definimos un valor por parámetro todos los que siguen deben tener también valores asignados por defecto:

# def devuelve_iterable(var1, var2, var3, var4=4, var5=5):
#     return var1, var2, var3, var4, var5

#en este caso no puedo traer un print(devuelve_iterable()) porque no tengo todos valores por defecto, si o si tengo que darle argumentos

# print('pepe','se','fue',sep=',') por defecto al final siempre hay un '\n', un salto de línea

# print('pepe','se','fue',sep=',', end=' ') 
# print('pepe','se','fue',sep=',', end=' ') acá no me hace el salto porque le asigno un end

#se recomienda hacer el retunrn y luego hacer el print por fuera. luego de llamar la función

#FORMAS DE PASAR VALORES A UNA FUNCIÓN

def cambio(valor):
    print(valor)
    valor= 'otro valor'
    print(valor)
    
valor='pepe'
cambio(valor)
print(valor)

#si no queremos que se pise el valor solamente se puede hacer cuando es dato compuesto y ahí si NO queremos que use la dirección de memoria tenemos que pasarle una copia

#como hago para poder pasarle los parametros que quiera a una función?

#quiero asignar yo valores y la cant que quiera

#ARGS
#args se utiliza por convención, podría utilizar cualquier nombre
#*args, lo importante es el *, lo que viene desp del * son los argumentos
#me permite pasarle los valores que yo quiera
#puede ser cualquier tipo de valor, strings, booleanos, etc


#cuando queremos pasarle valores pero decirle esto es tal cosa entra kwargs
#kwargs permite hacer algo similar pero en forma de diccionario, asignando llaves
#**kwargs uso para eso, lo importante son los dos *


