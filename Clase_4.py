

# if True:
#     print('No debería aparecer')
#     a = 15
#     b = 14
#     print(a + b)
# print('más código')

# primer_numero = int(input('Ingrese un numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# if primer_numero < segundo_numero:
#     print('El primer numero es menor al segundo')


nombre = input('Ingresar el nombre: ')

preferencia = input ('Ingresar tu preferencia, si te gusta Capcom ingresá la C y si te gusta Marvel ingresá la M: ')

if preferencia == 'M' and nombre<'M' or preferencia=='C' and nombre>'N':
    print('Sos grupo A')
else:    
    print('Sos grupo B')
    