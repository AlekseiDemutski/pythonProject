import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1q2w3e4r5t',
    database='sakila'
)

mycursor = mydb.cursor()

mycursor.execute('select * from actor where first_name like "%al%"')

myresult = mycursor.fetchmany(3)

print(myresult)
for data in myresult:
    print(data)
