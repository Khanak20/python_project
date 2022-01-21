def QUES():
    stud = int(input("How many students are there : "))
    
    for i in range(stud):
        stud_name = input("Enter student name : ")
        print(stud_name)
        subs = int(input("Write your total subjects number : "))
        print(subs)
        mark = []
        for j in range(subs):
            marks = input("Enter mark : ")
            int(marks)
            mark.append(marks)
        print(mark)
        for k in range(len(mark)):
            mark[k] = int(mark[k])
        print(sum(mark))    
    
    ques()

def ques():
    a = input("Are u want to enter the student data : ")
    if a == 'yes':
        QUES()
    else:
        exit()

QUES()
ques()