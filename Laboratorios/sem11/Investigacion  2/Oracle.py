#Para poder conectarse a una base de datos Oracle se necesita instalar el modulo cs_Oracle
import cx_Oracle
connection = cx_Oracle.connect('scott/tiger@orcl')
#Las acciones que se quieren realizar tendrian su lugar aqui
connection.close()

#Ejemplo
import cx_Oracle
conn_str='HR/HR@127.0.0.1:1521/XE'
db_conn = cx_Oracle.connect(conn_str)
cursor = db_conn.cursor()
cursor.execute('SELECT * FROM countries')
registros = cursor.fetchall()
for r in registros:
	print str(r)