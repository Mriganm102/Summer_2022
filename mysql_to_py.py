import matplotlib.pyplot as plt
import pymysql

import csv_to_df

conn = pymysql.connect(
    user='root',
    password='Soccer95;',
    host='127.0.0.1',
    database='guns',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

table_name = input("What is the table name?")
try:
    with conn.cursor() as cursor:
        # Read data from database
        sql = f"SELECT * FROM {table_name}"
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()
        list1 = list(rows[0])

        # Print results
        y_axis = []
        y_axis_two = []
        y_axis_three = []
        x_axis = []
        y_axis_four = []
        for row in rows:
            x_axis.append(row[list1[0]])
            y_axis.append(row[list1[1]])
            y_axis_two.append(row[list1[2]])
            y_axis_three.append(row[list1[3]])
            # y_axis_four.append(row[list1[4]])

        plt.plot(x_axis, y_axis, label=list1[1])
        plt.plot(x_axis, y_axis_two, label=list1[2])
        plt.plot(x_axis, y_axis_three, label=list1[3])
        #plt.plot(x_axis, y_axis_four, label=list1[4])
        plt.xlabel(list1[0])
        plt.ylabel(table_name)
        plt.legend(loc='upper right')
        plt.show()


finally:
    conn.close()