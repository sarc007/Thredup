import mysql.connector
conn = mysql.connector.connect(user='sadaf',password='Matrix@2018',host='localhost',database='thredup_db',auth_plugin='mysql_native_password')
mycursor = conn.cursor()
mycursor.execute('Select * from brandlist_tbl')
print(mycursor.fetchall())

