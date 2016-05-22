#desarrolle un programa que contenga dos funciones 
#la primera funcion debe permitir retornar la longitud de una cadena de caracteres 
#la segunda debe retornar la raiz de un numero dado
# el usuario debe escojer cual de las dos funciones se va a ejecutar 
#CESAR RAMIREZ C.I 23.951.089
from longitud import ValidaLongitud
from raiz import ValidaRaiz
opc='s'
while opc=='s':
	(print ('que desea Calcular'))
	operacion = (input ('1:longitud cadena de caracter, 2: raiz cuadrada '))
	if operacion =='1':
		longitud= (input ('ingrese cadena de caracteres'))
		(print ('la cadena tiene', ValidaLongitud(longitud),'caracteres'))
	elif operacion=='2':
		raiz= int(input ('ingrese numero cuya raiz quiere calcular'))
		(print ('la raiz del numero que ingreso es: ',ValidaRaiz(raiz) ))
	else:
		(print ('ingreso una opcion que no es valida'))
		opc= (input ('desea volver a intentarlo s/n'))
