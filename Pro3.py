# import mysql.connector as sql
# mycon = sql.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = '12345678',
#     database = 'NewDB1'
# )
# print(mycon)
# cursor = mycon.cursor()

# create table -------------------
# cursor.execute('CREATE TABLE Customer(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(150), email VARCHAR(150), mno VARCHAR(11))')
# print(cursor)

# Show All Avilable tables from database -------------
# cursor.execute('show tables')
# print(cursor)
# for i in cursor:
#     print(i)

# insert Data -----------------
# (1)
# cursor.execute('INSERT INTO Customer(name,email,mno) VALUES ("DArpan","darpan@gmail.com","876543290")')
# print(cursor)

# (2)
# nm = input("Enter Name = ")
# em = input("Enter Email = ")
# mno = input("Enter No. = ")

# values = (nm,em,mno)

# qu = "INSERT INTO Customer(name,email,mno) VALUES (%s,%s,%s)"
# cursor.execute(qu,values)


# (3)
# datas = [
#     ("Raj",'raj@gamil.com','6789054321'),
#          ("Rajshree",'rajshree@gamil.com','6789054322'),
#          ("meet",'meet@gamil.com','6789054323'),
#          ("Kishan",'kishan@gamil.com','6789054324'),
#          ("Vikas",'vikas@gamil.com','6789054325')
#          ]

# qu = "INSERT INTO Customer(name,email,mno) VALUES (%s,%s,%s)"
# cursor.executemany(qu,datas)

# print(cursor.rowcount)

# update Data -----------------
# (1)
# cursor.execute('UPDATE Customer SET name="Darshan", email="darshan@gmail.com" WHERE name="DArpan" ')
# print(cursor)

# (2)
# oldnm = input("Enter Old Name = ")
# newnm = input("Enter New Name = ")
# newem = input("Enter New Email = ")

# val = (newnm,newem,oldnm)

# que = 'UPDATE Customer SET name=%s, email=%s WHERE name=%s'
# cursor.execute(que,val)
# print(cursor)

# (3)
# datas =[
#     ('ABC','abc@gmail.com','meet'),
#     ('ABC','xyz@gmail.com','Kishan'),
#     ('ABC','tyu@gmail.com','Vikas')
# ]

# que = 'UPDATE Customer SET name=%s, email=%s WHERE name=%s'
# cursor.executemany(que,datas)
# print(cursor)

# delete Data -----------------
# (1)
# cursor.execute('DELETE FROM Customer WHERE id=8')
# print(cursor)

# (2)
# nm = input("Enter NAme To Delete Record = ")
# ids = int(input("Enter id To Delete Record = "))
# val = (nm,ids)
# qu = 'DELETE FROM Customer WHERE name=%s AND id=%s'
# cursor.execute(qu,val)
# print(cursor)


# nm = input("Enter NAme To Delete Record = ")

# val = (nm,)
# qu = 'DELETE FROM Customer WHERE name=%s'
# cursor.execute(qu,val)
# print(cursor)


# (3)

# val = [
#     ('Khanak','6'),
#     ('Raj','7')
# ]
# qu = 'DELETE FROM Customer WHERE name=%s AND id=%s'
# cursor.executemany(qu,val)
# print(cursor)


# # Fetch Data -----------------
# cursor.execute('select * from Customer')
# # print(cursor)
# data = cursor.fetchall()

# for i in data:
#     print(i)


# # Drop Table ---------
# cursor.execute('DROP TABLE Customer')
# print(cursor)

# # commit and close database
# mycon.commit()
# mycon.close()


# H/W
# (1) create product.csv file it contains fileds (id, prodnm, prodqty, prodprice)
# (2) insert product.csv data into mysql database table Product_details
# (3) fetch all data from Product_details database table
# (4) create products.json file from that data 

