import os
print("Bienvenido al supermercado ABC!")
lista= []
opcion=0;
contador = -1
while opcion != "4":
	print("1: Agregar objeto")
	print("2. Eliminar objeto")
	print("3. Ver lista")
	print("4. Salir")
	
	opcion=input("Por favor eliga una opcion: ")
	
	if opcion == "1":
		objeto=input("Que desea agregar? ")
		contador = contador + 1
		objeto = (str(contador) + "." + str(objeto))
		lista.append(objeto)
	if opcion == "2":
		print(lista)
		eliminar = int(input("Que desea quitar de la lista? \(si es la 2da vez que quita un ojeto, restele 1 al indice del elemento"))
		print("Se a eliminado el elemento: " + lista[eliminar])
		del lista[eliminar]
	if opcion == "3":
		print(lista)
	
	print("Pulse enter para continuar")
	input()
	os.system("cls")	