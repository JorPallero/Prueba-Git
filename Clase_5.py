#while True:
    # print('Se ejecuto el print')
    
""" while False:
    print('No salimos más de acá...')   """
    
""" ejecucion_nro = 0
while True:
    ejecucion_nro += 1
    print('Se ejecuto el print nro:', ejecucion_nro) """
    
repetir_menu = True #bandera/flag
while repetir_menu:
    print('''
==================
    Menu
==================
1. Retirar efectivo
2. Cambiar contraseña
3. Salir
''')
    opcion_elegida = input('Ingrese la operacion a realizar: ')
    if opcion_elegida == '1':
        print('Retiro efectivo')
    elif opcion_elegida == '2':
        print('Cambio de contraseña')
    elif opcion_elegida == '3':
        print('Hasta luego')
        repetir_menu = False
    else:
        print('Vuelva a intentar con una opción válida')

""" numeros = [14, 45, 5, 1234, 1, 4, 9, 15, 25]
valor_ext=0
while valor_ext != 5:
    valor_ext = numeros.pop()
    print(valor_ext) """
    
""" hasta = int(input('Ingrese un num hasta donde quiere sumar: '))
suma = 0
while hasta:
    suma += hasta
    hasta -= 1
    
print(f'la suma es {suma}') """

""" numero = 0
while numero < 10:
    numero += 1
    if numero %2 == 0:
        continue #se saltea el resto de lo que hay en el bloque de código
    print(numero)
    
print('Sali del while') """


