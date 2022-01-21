import csv

files = {}
def files():
    print(files)



def QUES():
    print('''
    [1 for create csv file] [2 for view] [0 for Exit]''')
    que = input("What u want : ")
    if que == "1":
        create()
    elif que == "2":
        view()
    elif que == "0":
        exit()
    else: 
        QUES() 


def create():
    csv1 = '.csv'
    csv_name = input('Enter your csv file name : ')
    fnm = print(csv_name+csv1)
    files = open(csv1,'w')

    field_range = int(input('How many field you want to enter : '))
    for i in range(field_range):
       key_files = input("Enter field name : ")
    wr1 = csv.DictWriter(files,key_files)
    wr1.writeheader()

    value_range = int(input('How much data you want to enter : '))
    for j in range(value_range):
        files[key_files] = print('Enter your value for ' , key_files)
    wr1 = csv.DictWriter(files,files[key_files])
    wr1.writerow()


    files.close()
    QUES()

def view():
    print("Your saved csv files are : ")
    files()
    file2 = input('Enter file name : ')
    if file2 == files :
        data1 = open(file2,'r')
        read1 = csv.DictReader(data1)
        print(read1)
        file2.close()
        QUES()
    else:
        print("No such file is here.")
        QUES()


QUES()
create()
view()