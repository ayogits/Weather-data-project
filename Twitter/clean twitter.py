import pyodbc

cnx = pyodbc.connect('DSN=kubricksql')
cursor = cnx.cursor()

cursor.execute("select * from [dbo].[Tweetdb]")
for row in cursor.fetchall():
    print row