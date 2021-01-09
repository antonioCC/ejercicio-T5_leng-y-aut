import re
#patron = re.compile('a[3-5]+')# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
#print( input("Introduce un texto") );
archivo=open('datos2.txt','r')
#print("el texto es: "+archivo.read())
mensaje=archivo.read()


print("ingresa un una opcion")
print("1: sentencia de asignacion")
print("2: operaciones aritmeticas basicas")
print("3: expresiones booleanas basicas")
print("4: formulas mas complejas")
print("5: palabras reservadas")
numero = int(input())

if numero==1:
	#sentencia de asignacion
	patron = re.compile('[A-Za-z]+\w?\=[A-Za-z0-9]+\w?\;')
	print (patron.findall(mensaje))
	archivo.close()


if numero==2:
	#operaciones aritmeticas basicas
	patron = re.compile('([A-Za-z]+\w?\=\-?([A-Za-z0-9]+\w?|\d{1,7}(\.\d{1,7})?)(\+|\-|\*|\/)\d{1,7}(\.\d{1,7})?\;)')
	print (patron.findall(mensaje))
	archivo.close()

if numero==3:
	#expresiones booleanas basicas
	patron = re.compile('([A-Za-z]+\w?(\<|\>|\=\=|\<\=|\>\=|\!\=)\-?([A-Za-z]+\w?|\d{1,7}(\.\d{1,7})?))')
	print (patron.findall(mensaje))
	archivo.close()

if numero==4:
	#formulas mas complejas
	patron = re.compile('([A-Za-z]+\w?\=\!?([A-Za-z]+\w?|\d{1,7}(\.\d{1,7})?)(\||\&)\!?[A-Za-z]+\w?\;)')
	print (patron.findall(mensaje))
	archivo.close()

if numero==5:
	#palabras reservadas
	patron = re.compile('if|else|double|print|while|for|int|String|do|boolean')
	print (patron.findall(mensaje))
	archivo.close()

