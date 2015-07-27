#La función pymssql.connect se usa para conectarse a la base de datos SQL
import pymssql
conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')

#La función cursor.execute puede usarse para recuperar un conjunto de resultados de una consulta realizada a la base de datos SQL. Esta función acepta cualquier consulta y devuelve un conjunto de resultados que se puede iterar mediante el uso de cursor.fetchone().
import pymssql
conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')
cursor = conn.cursor()
cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')
row = cursor.fetchone()
while row:
    print str(row[0]) + " " + str(row[1]) + " " + str(row[2])   
    row = cursor.fetchone()
	
#En la base de datos SQL, la propiedad IDENTITY y el objeto SEQUENCE pueden usarse para generar automáticamente los valores de clave principal.
import pymssql
conn = pymssql.connect(server='yourserver.database.windows.net', user='yourusername@yourserver', password='yourpassword', database='AdventureWorks')
cursor = conn.cursor()
cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express', 'SQLEXPRESS', 0, 0, CURRENT_TIMESTAMP)")
row = cursor.fetchone()
while row:
    print "Inserted Product ID : " +str(row[0])
    row = cursor.fetchone()