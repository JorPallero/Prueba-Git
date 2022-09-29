nombre=input("Ingrese su nombre por favor: ")
preferencia= input("Ingrese su preferencia, M para Marvel y C para Capcom: ")

if preferencia == "M" and nombre < 'M' or preferencia == "C" and nombre > 'N':
    print ('Perteneces al grupo A')
else:
    print('Perteneces al grupo B')
    