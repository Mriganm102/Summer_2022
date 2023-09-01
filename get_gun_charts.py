import pandas as pd
import csv
import mysql.connector
import matplotlib.pyplot as plt
import pymysql
import os


file = open('gun_data.csv')
csv_data = csv.reader(file)



conn = mysql.connector.connect(user='root', password='Soccer95;', host='127.0.0.1', database='guns')

mycursor = conn.cursor()
skipHeader = True

column_names_old = []
column_names = []
for i in csv_data:
    column_names_old = i
    break

column_names_old[0] = column_names_old[0][3:]
for i in column_names_old:
    i = list(i.split(" "))
    empty_str = ""
    if len(i) == 1:
        for j in i:
            empty_str += j
            column_names.append(empty_str)
        continue
    a = "_".join(i)
    column_names.append(a)

column_names = tuple(column_names)
tablename = input('What do you want the table name to be?')

create_columns = str((len(column_names) - 2) * " %s int not null,")
create_table_query = f"CREATE TABLE {tablename} (%s year not null," + create_columns + " %s int not null)"
create_table_query = create_table_query % column_names



mycursor.execute(create_table_query)
conn.commit()

for data_row in csv_data:
    # if skipHeader:
    #     skipHeader = False
    #     continue
    for j in range(1, len(column_names)):
        data_row[j] = int(data_row[j])
    data_row[0] = data_row[0][:4]
    data_row = tuple(data_row)
    sql = f"INSERT INTO {tablename} VALUES (" + (((len(column_names) - 1) * '%s,') + '%s)')
    mycursor.execute(sql, data_row)

conn.commit()

try:
    with conn.cursor() as cursor:
        # Read data from database
        sql = f"SELECT * FROM {tablename}"
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()
        column_names = list(next(zip(*cursor.description)))

        # Print results
        x_axis = []
        y_axis = []
        for i in rows:
            x_axis.append(i[0])
        for j in range(1, len(column_names)):
            try:
                for i in rows:
                    y_axis.append(i[j])
            except IndexError:
                pass
            plt.plot(x_axis, y_axis, label=column_names[j])
            y_axis = []

        plt.xlabel(column_names[0])
        plt.ylabel(tablename)
        plt.legend(loc='upper right')
        fig1 = plt.gcf()
        plt.show()

        fig1.savefig(f'{tablename}.png')
        os.rename(fr"C:\Users\ashmr\PycharmProjects\Summer_2022\{tablename}.png", fr"C:\Users\ashmr\PycharmProjects\Summer_2022\gun_stats_graphs\{tablename}.png")


finally:
    conn.close()

