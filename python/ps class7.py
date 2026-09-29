#procedure oriented programming-->functions--> a function is a block of code that performs a specific task,
#we have a keyword def.
'''
syntax:
def fname(parameters):#define function
"""Doc String(describe ur function)"""
    statement(s)...
    ....            #body of func
    ....
    return value(s)...
fname(args)#function call

def intro():
    """intro to functions"""
    return" hope ur learning nd enjoying the journey"
print(intro())

#positional arguements,keyword arguements,default arguements,variable length arguements,keyword variable length arguements
def add(a,b):
    """simple addition function"""
    return a+b
print(add(5,7))#addition
print(add('codegnan','python'))#concat
print(add([1,2,3],[4,5,6]))#merging
c,d=map(int(input("enter the values").split(',')))
print(add(c,d))

#print(add(9,8,9,4))raises typerror as positional arguements didnt match
#positional arguements:- order of arguements in function definition nd function call should match
#keyword arguements:-- name of the arguements should match

def grocery(item,price):
    """keyword arguement usage"""
    print(f'item is {item}')
    print(f'price is{price}')
grocery("milk",35)
print(grocery(price=45,item="bread"))#it also returns 'none' as ntg to b printed
'''
def grocery(item="jam",price=50):
    """keyword arguement usage"""
    print(f'item is {item}')
    print(f'price is{price}')
grocery("milk",35)
grocery("bread")
grocery()
