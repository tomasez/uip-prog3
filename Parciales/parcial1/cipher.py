import os
cifrado=""
descifrado=""
texto_descifrado=""
opcion="0"
while opcion != '5':
	print("1. Agrege un texto")
	print("2.Cifre el texto")
	print("3. Descifre el texto")
	print("4. Imprima el texto original")
	
	if opcion == '1':
		texto = input("Ingrese el texto que quiere almacenar: ") 
	if opcion == '2':
		for i in texto:	cifrado=cifrado+(ord(i)+1) 
		descifrado=descifrado+chr(cifrado-1)
		texto_descifrado = texto_descifrado+descifrado
	if opcion == '3':
		print(texto_descifrado)
	if opcion == '4':
		print(texto)
	
	opcion = input("Eliga una accion: ")
	os.system("cls")