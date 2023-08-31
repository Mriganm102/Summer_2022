import matplotlib.pyplot as plt
import pymysql
from colorama import Fore

import csv_to_mysql

conn = pymysql.connect(
    user='root',
    password='Soccer95;',
    host='127.0.0.1',
    database='mass_towns',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


try:
    with conn.cursor() as cursor:
        # Read data from database
        sql = f"SELECT * FROM {csv_to_mysql.table_name}"
        cursor.execute(sql)

        # Fetch all rows
        rows = cursor.fetchall()

        # Print results
        x_axis = []
        y_axis = []
        percent_change = []
        for row in rows:
            row['id'] = int(row['id'])
            row['prev_year_houses_sold'] = int(row['prev_year_houses_sold'])
            row['cur_year_houses_sold'] = int(row['cur_year_houses_sold'])
            row['percent_change'] = row['percent_change'][:-1]
            row['percent_change'] = abs(float(row['percent_change']))
            percent_change.append(row['percent_change'])
            x_axis.append(row['prev_year_houses_sold'])
            y_axis.append(row['cur_year_houses_sold'])
        plt.scatter(x_axis, y_axis)
        plt.xlabel('prev_year_houses_sold')
        plt.ylabel('cur_year_houses_sold')
        plt.show()
        for i in rows:
            a = i['town']
            if i['percent_change'] == max(percent_change):
                print(Fore.GREEN + f'Maximum change in {a}')
            if i['percent_change'] == min(percent_change):
                print(Fore.RED + f'Minimum change in {a}')

finally:
    conn.close()