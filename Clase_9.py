#funciones

# cant_letras=0
# for letra in 'Hola':
#     cant_letras+=1
    
# print(cant_letras)


#print, len son funciones preestablecidas

#def NOMBRE(PARAMETROS): #correcto nombramiento de las funciones
    #SENTENCIAS
    #return EXPRESION (este return puede existir o no y puede o no tener una expresion asociada)
    
#las funciones se nonbran con todas letras en minúsculas con _ para separar palabras y numeros siempre que no estén al inicio

    
# def mostrar_palabra(): #entre ()pueden ir o no ir los parámetros
#     print('Perro')
    
# mostrar_palabra() #si o si con () para que sea función
# valor_retornado=mostrar_palabra()
# print(valor_retornado)

valor1=4 #las funciones pueden utilizar valores externos (esten antes o desp de la función) si están antes del llamado de la función

#pero los valores definidos dentro de la función no se pueden utilizar por fuera
#si hubiese dos valor1, uno dentro y otro fuera, queda el que está dentro porque para una función tiene más valor una variable interna que una externa
def sumar_numeros():
    valor2=56
    valor3=15
    return valor1 + valor2 + valor3

suma_de_valores=sumar_numeros()#lo que va entre ( ) cuando llamo la función es el argumento

#en l definición se llaman parámetros lo que va entre ()

def contame_las_letras(palabras_a_contar): #entre()el parámetro
    cant_letras=0
    for letra in palabras_a_contar:
        cant_letras+=1
    return cant_letras
print(contame_las_letras('ricardo'))#entre ()el argumento


# momentos de una función
# definimos la función
#llamo a la función, ejecuta su código
#revisar si hay un return
#si no tiene un return devuelve none por defecto
#si tiene return devuelve lo que tiene a continuación 


# Ejercicio Par o Impar

def par_o_impar(numero):
    if numero%2==0:
        return 'Par' #o puedo poner print('Par')
    else:
        return 'Impar' #o puedo poner print('Impar')
        
print(par_o_impar(int(input('ingresame un número y te digo qué es: '))))






