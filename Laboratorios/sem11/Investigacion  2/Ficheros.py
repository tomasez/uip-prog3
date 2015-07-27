#Python nos proporciona diferentes maneras de leer un fichero. En primer lugar podemos leer un fichero completamente usando la función f.read():

# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
infile = open('texto.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Lectura completa del fichero')
print(infile.read())
# Cerramos el fichero.
infile.close()

#También podemos optar por leer una cantidad determinadas de bytes del fichero usando la función f.read(size):

# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
infile = open('texto.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Lectura de una cantidad determinada de bytes')
print(infile.read(50) + '\n')
# Cerramos el fichero.
infile.close()

#Podemos optar por leer una única línea del fichero con la función f.readline():

# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
infile = open('texto.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Lectura de una línea del fichero')
print(infile.readline())
# Cerramos el fichero.
infile.close()

#Por último, podemos leer un fichero completo línea a línea de la siguiente manera:


# En primer lugar debemos de abrir el fichero que vamos a leer.
# Usa 'rb' en vez de 'r' si se trata de un fichero binario.
infile = open('texto.txt', 'r')
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Lectura del fichero línea a línea')
for line in infile:
    print(line)
# Cerramos el fichero.
infile.close()

#Para escribir un fichero en Python tendremos básicamente dos opciones que vamos a ver a continuación. Primero podemos escribir un fichero sobreescribiendo el contenido del fichero:

outfile = open('texto.txt', 'w') # Indicamos el valor 'w'.
outfile.write('Fusce vitae leo purus, a tempor nisi.\n')
outfile.close()
# Leemos el contenido para comprobar que ha sobreescrito el contenido.
infile = open('texto.txt', 'r')
print('>>> Escritura de fichero sobreescribiendo su contenido.')
print(infile.read())
# Cerramos el fichero.
infile.close()

#O podemos concatenar el nuevo contenido al contenido ya existente en el fichero:

outfile = open('texto.txt', 'a') # Indicamos el valor 'w'.
outfile.write('Fusce vitae leo purus, a tempor nisi.\n')
outfile.close()
# Leemos el contenido para comprobar que ha sobreescrito el contenido.
infile = open('texto.txt', 'r')
print('>>> Escritura de fichero concatenando su contenido.')
print(infile.read())
# Cerramos el fichero.
infile.close()