print("Bienvenido al sistema de comiciones\nPor favor ingrese su nombre y ventas")
nombre=input("Nombre: ")
venta1=float(input("Venta 1: "))
venta2=float(input("Venta 2: "))
venta3=float(input("Venta 3: "))
tventas=(venta1+venta2+venta3)
comision=((tventas)*12.5)/100
tcomision=tventas+comision
print("\nVendedor\tVentas\tComision")
print(nombre + "\t\t" + str(venta1)) 
print(nombre + "\t\t" + str(venta2)) 
print(nombre + "\t\t" + str(venta3))
print("\t\t\t" + str(comision))
print("\nTotal ventas\t Total+Comision")
print(str(tventas) + "\t\t " + str(tcomision))
input()