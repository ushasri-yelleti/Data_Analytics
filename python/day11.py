a = 90
b = 780
c = 670
if a>b and a>c;# 90 > 780 and 90 > 67
    print(a)
elif b>a and b>c:#780 > 90 and 780 > 67
    print(b)
    else:
        print(c)

num = 7
num_2 = 3
user_opt = int(input('enter \n1.add \n2.sub \n3.mul \n4.pow:')
if user_opt == 1:
    print(num + num_2)
elif user_opt == 2:
    print(num - num_2)
elif user_opt == 3:
    print(num * num_2)
else:
    print(num ** num_2)

#nested if (if inside one more if is called nested if):--
import random
user_pass = int(input("enter ur password:"))
if user_pass == app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp = int(input("enter 4 digits otp:"))
    if user_otp == otp:
        print('welcome to the app')
    else:
        print('incorrect otp')
else:
    print('password is incorrect')

#even&odd:--
a = int(input("enter a number:"))
if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

#grading system:--
marks_ = int(input("enter ur marks:"))
if marks_ >=90:
    print('a+')
elif marks_ >=80:
    print('a')
elif marks_ >=70:
    print('b+')
elif marks_ >=60:
    print('b')
elif marks_ >=50:
    print('c+')
elif marks_ >=40:
    print('c')
else:
    print('fail')
     
        
