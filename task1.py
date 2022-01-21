import csv
import json
import mysql.connector as sql
mycon = sql.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    passwd = '12345678',
    database = 'prod_info'
)

cursor = mycon.cursor()
csv_file = open('E:/python program/MY_SQL_DATA/task/proddetail.csv','r')
reader = csv.reader(csv_file)
print(reader)

for row in reader:

    cursor.execute("INSERT INTO prod_info.prod_table(prodnm,prodpr,prodqt) VALUES(%s, %s, %s)",tuple(row))
    row = cursor.fetchall()
    mycon.commit()
    cursor.execute("select * from prod_table")
    row = cursor.fetchall()

    file_json = json.dumps(dict(row))
    print(file_json)

csv_file.close()
print("done")

