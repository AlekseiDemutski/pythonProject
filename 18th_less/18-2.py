import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1q2w3e4r5t',
    database='sakila'
)

df = pd.read_sql_query('select * from film', conn)
print(df)