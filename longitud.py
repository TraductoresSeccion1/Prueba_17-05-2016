#CESAR RAMIREZ C.I 23.951.089
def ValidaLongitud(longitud):
	if ' ' in longitud:
		return 'la cadena de caracteres no debe contener espacios'
	else:
		return len(longitud)