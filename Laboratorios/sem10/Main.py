import os,Lector,Autor,Copia,Libro #Importa las clases
lista_lectores = []	#Declaramos las listas
lista_autores = []
lista_libros = []
opcion=""

while opcion != "6":	#Este es el menu
	print("1. Ingresar un lector: ") 
	print("2. Ingresar un autor: ")
	print("3. Ingresar un libro: ")
	print("4. Hacer peticion: ")
	print("5. Hacer devolucion: ")
	print("6. Salir")
	opcion=input("Ingrese una opcion: ")
	print("\n")
	if opcion=="1":
		ID = input("Ingrese el ID: ")
		nombre = input("Ingrese su nombre: ")
		lector = Lector.Lector(ID,nombre)	#Declaramos un objeto
		lista_lectores.append(lector)
		os.system("cls")
		
	if opcion=="2":
		nombre2=input("Ingrese el nombre del autor: ")
		nacionalidad=input("Ingrese su nacionalidad: ")
		autor = Autor.Autor(nombre2,nacionalidad)	#Declaramos un objeto
		lista_autores.append(autor)
		os.system("cls")
		
	if opcion=="3":
		titulo = input("Ingrese el titulo: ")
		tipo = input("Ingrese el tipo: ")
		editorial = input("Ingrese la editorial: ")
		libro = Libro.Libro(titulo,tipo,editorial)	#Declaramos un objeto
		lista_libros.append(libro)
		contador = 10
		os.system("cls")
		
	if opcion=="4":
		contador-=1
		if contador<0:
			os.system("cls")
			print("No hay mas libros.\n")
		else:
			os.system("cls")
			print("Se ha retirado un libro.\n")
			
	if opcion=="5":
		contador+=1
		if contador>10:
			os.system("cls")
			print("No hay libros que devolver.\n")
			contador-=1
		else:
			os.system("cls")
			print("Se ha devuelto el libro.\n")