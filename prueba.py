#Desarrolle un programa que contenga dos funciones
#1. Debe permitir retornar la longitud de una cadena de caracteres.
#2. Debe retornar la raiz cuadrada de un numero dado
#El usuario debe elegir cuan de las 2 funciones se debe ejecutar.


import math
opc = 's'

while opc == 's':

	operacion = raw_input('Que desea realizar: 1. Calcular longitud. 2.Calcular raiz cuadrada ')
	if operacion == '1':
		palabra = raw_input('Ingrese una palabra: ')
		print 'La longitud es: '
		print  len(palabra)

	elif operacion == '2':

		num = input('Ingrese Numero: ')
		raiz = math.sqrt(num)
		print 'La raiz cuadrada es: '
		print raiz

	opc = raw_input('Desea continuar: (S/N): ')


#Cesar, Requena C.I 20.878.837