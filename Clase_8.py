#dos formas de abrir un archivo:

archivo_abierto=open('C:\Users\jor_p\04_Coder\Projects\Clase_8.py','w') #'w' indica qué se quiere hacer con ese archivo

#'w'permite abrir el archivo para escribirlo. la 'r' para llerlo y la 'a' para escibirlo pero de manera distinta
#cuando abrimos un archivo de esta manera necesitamos guardarlo para poder trabajarlo por eso lo asignamos a una variable
#desp de trabajar necesitamos hacerle un close:

archivo_abierto.close()

#Otra dorma de abrir:

with open('C:\Users\jor_p\04_Coder\Projects\Clase_8.py','w') as archivo_abierto:
    #de esta forma no necesitamos cerrarlo, 
    #se cierra solo con el with con identación
    #una vez que quedamos fuera de la identación se cierra solo
   
    
#como hacemos para escribirlo:'w' (write)

#cuando queremos abrir un archivo con 'w' y no existe ese archivo, lo crea

#open crea solamente archivos, no carpetas

#la w nos permite escribir pero sobreescribe, si hay algo antes lo pisa entero

#pero puedo escribir varias cosas con un write.('')

#cada write escribe a continuación de los anterior agregado, por eso usamos \n

#el close nos asegura que el archivo quede cerrado para futuros usos

#open permite paarle entre () la ubicaciób del archivo y abrirlo

#'w' me permite escrinir una línea detrás de la otra

#si vuelvo a ejecutar un write pisa el archivo

#con with open cierra solo el archivo

#qué pasa si no quiero que se pise lo que estaba antes, puedo iusar 'a'

#para leer usamos 'r' (read)

#read devuelve el texto que está guardado en el archivo

#hay tipo de carácteres que no los tiene en cuenta, emtonces hay que determinarle al open que utilice encoding="utf-8"

#si le agrego al read un print('----------') y luego lo leo nuevamente agrega eso al final

#un readline devuelve la primer línea siempre

#cuando yo abro un archivo lo tengo entero para su uso

#si hago 3 readlines muestra tres líneas, si hay espacios vacíos entre líneas lo tiene en cuenta como línea

#readlines devuelve una lista de cada tipo de oración, no es un string, nos devuelve una lista con cada línea como elementos que la componen

#readline devuelve \n como un elemento más

#hay una funcionalidad que nos permite ubicar el cursor: seek en lugar de read

#seek le podemos pasar una ubicación (), desde donde queremos que empiece, la primer ubicación es 0

#tengo el archivo abierto, debo usar un open y un read y luego uso el seek para que con ese archivo abierto me ubique el puntero en la ubicación que le indico

#seek se utiliza con read, con readline,




