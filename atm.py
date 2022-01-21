class atm_machine:
    def __init__(self):
        self.x=500
        print("Your current balance is : " , self.x)
  
    def deposit(self):
        y=int(input("Enter amount to be Deposited: "))
        self.x += y
        print("\n Your current balance is : " , self.x)
  
    def withdraw(self):
        y = int(input("Enter amount to be Withdrawn: "))
        self.x -= y
        print("\n Your current balance is : " , self.x)
  
    def view(self):
        print("\n Net Available Balance=",self.x)
  
# Driver code
   
# creating an object of class
a = atm_machine()
print("""Press '1' for Deposite.
        Press '2' for withdraw.
        Press '3' for view your current balance.""")
def operation():
    
    b = int(input("What u want to do : "))
    if b == 1:
        a.deposit()
        operation()
    elif b == 2:
        a.withdraw()
        operation()
    elif b == 3:
        a.view()
        operation()
    else:
        operation()

operation()
a.deposit()
a.withdraw()
a.view()




