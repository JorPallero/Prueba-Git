# def dividir(a,b):
#     return a/b

# print(dividir(5,7))

# #cómo hago para dividir por cero? y que no de error

# def dividir(a,b):
#     if b==0:
#         return None
#     return a/b

# print(dividir(5,0))

# def dividir(a,b):
#     if b!=0:
#         return a/b
    
# Hay otras formas de protegernos de errores sin hacer este tipo de validaciones:
#no podemos hacer un if por cada bloque de código

#MANEJO DE ERRORES/EXCEPCIONES INCORPORADAS

#VER
#docs.python.org/es/3/library/exceptions.html

#la mayoría están dentro de la rama "Exception"

#try - except

try:
    ...
except:
    ... #los '...' simula que hay código 
    
def dividir(a,b):
    try:
        return a/b
    except:
        return 'No se puede dividir por 0'
    
print(dividir(5,0))
print(dividir('5',5)) #indistintamente del error va a devolver el mismo error


# valor=15
# print(valor)

# try:
#     valor*=15
#     print(valor)
#     valor+=15
#     print(valor)
#     valor/=0
#     print(valor)
#     valor-=15
#     print(valor)
    
# except:
#     print('se generó un error')
    
#en el código anterior corta cuando llega al error

#Puedo hacer que cuando se genera el error no se corte el bloque de código:



#else

# a=5
# b=0

# try:
#     valor=a/b
# except:
#     print('No se puede dividir por 0')
# else:
#     print(f'La dividiom dio como resultado {valor}')
    
#el else se va a ejecutar cuando no se ejecute el except


# a=5
# b=1
# c=0

# try:
#     valor=a/b
# except:
#     # valor=a/c
#     print('No se puede dividir por 0')
# else:
#     valor /=c
#     print(f'La division dio como resultado {valor}')
    
#esto da error 

#se pueden trabajar con try-except anidados


#finally: por fuera dem lo que ocurra el try agregamos el finally 

#permite a diferencia del else ejecutarse pase por el try o pase por el except o pase por el try y pase por el else

#finally se ejecuta siempre

#se puede utilizar por ejemplo cuando abro un archivo y em lugar de ponerle un close al final del trry, except y else, le pongo un finally con el close y listo


#excepciones multiples

#type().__name__

# __name__nos permite traer el typo sin el class y nos permite comparar, por ejemplo poner==int, ==str, etc

#except Exception as error:  "exception" es una excepción de python predefinida

#cuando venga un exception agarramos el error con un except

#el exception más especifico debe ir primero, luego los que abarcan más excepciones dentro

#cuando entra en un except, los demás ya no los tiene en cuenta





    

    



