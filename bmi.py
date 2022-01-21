name = input("Enter your name : ")
height = float(input("Enter your height in cm : "))
weight = float(input("Enter your weight in kg : "))

# bmi_calculator

def bmi_calculator(name,height,weight):
   bmi = weight / ((height*0.01) ** 2)
   print("bmi: ")
   print(bmi)
   if bmi < 16:
       return name + (" is severely underweight.")
   elif (bmi >= 16 and bmi < 18.5):
       return name + (" is underweight.")  
   elif (bmi >= 18.5 and bmi < 25):
       return name + (" is healthy.")  
   elif (bmi >= 25 and bmi < 30):
       return name + (" is overweight.")         
   else :
        return name + (" is obese.")   

result = bmi_calculator(name,height,weight)

print(result)