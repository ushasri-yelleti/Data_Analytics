'''
input()-- input formatting
print()-- output formatting(f string)
a,b = 13,4.5
print(9,5,sep=',')
print(9,5,sep=';')
print(a,b,end=' ')
print("codegnan is in vizag",end='\t')
print("pfs6 and da6")
print()
print('-----> welcome to game----->')
a,b= map(int,input("enter the values").split(','))
addition = a+b
substraction = a-b
multiply = a*b
divide = a/b
print("-----> calculator----->")
print("allows only +,_,*,\,")
print()
print("addition result is",addition)
print("substraction result is",substraction)
print("multiply result is",multiply)
print("divide result is",divide)
print()
#usage of %d,%f,%s-- prefer these only when we r working on calculations
#print("usage of%"%(args))
price = 45.3;grade = 'A';stock = 15
print("%d"%price)
#print("%d"%grade) #typeerror
#print("price is %d"%price)
print("price is %.f"%price)
print("price is %.1f"%price)
print("grade is %s"%grade)
#area of circle= 3.5cm,round off the area to 2 decimal values: take pi value as 3.14
pi = 3.14
radius = 3.5
area= pi*(radius**2)
print("area of circle is %.2f"%area)
#new style formatting--> fstring
name="codegnan";batch="da6"
print(f'{batch} is in {name}')
#control statements--> they cntrl the flow of the progrm, divided into 3 types:
#conditional statements(if,else,elif)
#repetition statements(loops)(for,while)
#jumping statements(break,continue,pass)
#bmi calculator
weight = int(input("enter the weight in kgs:"))
height = float(input("enter the height in meters:"))
name = input("enter name:")
bmi = weight / ((height)**2)
print(bmi)
if bmi<18.5:
    print(f'bmi of {name} is {bmi} and u r underweight...eat well')
elif bmi>=18.5 and bmi<=24.9:
     print(f'bmi of {name} is {bmi} and u r healthy...be consistent')
elif bmi>=25 and bmi<=29.9:
     print(f'bmi of {name} is {bmi} and u r overweight...start excercising')
elif bmi>30:
     print(f'bmi of {name} is {bmi} and u r obese...')
else:
     print("do enter only +ve values greater thn 0")
'''
 # task:-- user can enter height in cm,feets --> metres
 #cal bmi
 #make all user validations fr height--> cms,feets
weight = float(input("Enter the weight in kgs: "))
name = input("Enter name: ")

print("\nChoose your height unit:")
print("1. Metres")
print("2. Centimetres")
print("3. Feet")

choice = int(input("Enter your choice (1/2/3): "))

if weight <= 0:
    print("Please enter a positive weight greater than 0.")

elif choice == 1:
    height = float(input("Enter height in metres: "))
    if height <= 0 or height > 2:
        print("Please enter a positive height within limits.")
    else:
       height = height
elif choice == 2:
    height_cm = float(input("Enter height in centimetres: "))

    if height_cm <= 0:
        print("Please enter a positive height greater than 0.")
    else:
        height = height_cm / 100
        #bmi = weight / (height ** 2)

elif choice == 3:
    height_feet = float(input("Enter height in feet: "))

    if height_feet <= 0:
        print("Please enter a positive height greater than 0.")
    else:
        height = height_feet * 0.3048
        #bmi = weight / (height ** 2)
    print("BMI Calculation")
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print(f"BMI of {name} is {bmi:.2f} and you are underweight... eat well")
    elif bmi <= 24.9:
        print(f"BMI of {name} is {bmi:.2f} and you are healthy... be consistent")
    elif bmi <= 29.9:
        print(f"BMI of {name} is {bmi:.2f} and you are overweight... start exercising")
    else:
        print(f"BMI of {name} is {bmi:.2f} and you are obese...")
