#Verificar puertos TCP abiertos
import socket
import getopt
import sys

def check(ip, port):
	gotod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		gotod.settimeout(5)
		gotod.connect((ip, int(port)))
		gotod.shutdown(2)
		gotod.close()
		return True
	except:
		return False


arguments = {}
options, remainder = getopt.getopt(sys.argv[1:], 'h:p:')
for opt, arg in options:
	arguments[opt] = arg

if ('-h' in arguments) and ('-p' in arguments):
	status = False

	status = check(arguments['-h'], arguments['-p'])

	if status:
		print ('Puerto abierto')
	else:
		print ("Puerto cerrado")
else:
	print ('Faltan parametros')