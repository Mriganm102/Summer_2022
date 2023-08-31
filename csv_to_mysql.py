import csv
import mysql.connector


conn = mysql.connector.connect(user='root', password='Soccer95;', host='127.0.0.1', database='mass_towns')

file = open('df_to_csv.csv')
csv_data = csv.reader(file)
print(csv_data)

mycursor = conn.cursor()
skipHeader = True
table_name = input("Table Name: ")

delete_all_rows = f"truncate table {table_name}"
mycursor.execute(delete_all_rows)
conn.commit()

for row in csv_data:
    if skipHeader:
        skipHeader = False
        continue
    row = tuple(row)
    sql = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, row)

conn.commit()
