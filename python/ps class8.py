'''
#scope of variable:--
scope is basically the region or area wr the data is accessible
#local scope,global scope,global keyword,enclosing scope(non local keyword)
built in scope

def data():
    """local scope"""
    name="codegnan"
    return f'{name} is in vizag'
print(data())
#global scope-- variables defined outside the function can be accessible inside the function also

count=10 #global variable
def details():
    """global scope"""
    print(f'value of count is{count} inside the function')
details()
print(f'value of count is{count} outside the function')

count=10 #global variable
def details():
    """priority of local vs global"""
    count=15 #local variable
    print(f'value of count is{count} inside the function')# this results in 15 becoz, this statement is passed inside the function; in such cases it will prioritize local variable over global
    count=count+5
details()
print(f'value of count is{count} outside the function')# it gives 10 because, it is called outside the function

#usage of global
count=10
def details():
    """usage of global keyword"""
    global count
    count= count+15
    print(f'value of count is{count} inside the function')
details()
print(f'value of count is{count} outside the function')

#enclosing scope--> nested functions
def outer():
    """nested functions"""
    count=5
    def inner():
        """inner function to use count var"""
        nonlocal count
        count=count*4
        print(f'value of count is {count} inside the function')
    inner()
    print(f'value of count is {count} outside the function')
outer()

#built in scope--> usage of built in functions as variables
len =13
print(len)
a=['codegnan','python','data']
print(len(a))# raises typeerror

#LEBG rule--> local,enclosing,builtin,global
#import this
#built in functions,anonymous functions,recursive functions

#print(dir())
print(dir(__builtins__))#returns the list of all built-ins(functions,errors)
#every built in datatype is a built in function-->int,float,str,list,tuple,set,dict,bool

print(bool('codegnan'))#returns boolean val- True
print(float(int(bool(24))))
print(abs(-23))#returns the absolute value

#none,'',0,false,[],(),{} #empties
#all(),any()
x=[23,45,'poll']
x.append(None)
print(x)
print(all(x))
print(any(x))

print(bin(12))#gives the binary value of the given no.
print(chr(67))#gives the concerned object/value; which is capital c
print(ord('A'))#gives the ascii value 

#print(),type(),len(),min(),max()
print(divmod(6,2))#performs 6//2--> which gives 3 quotient nd 0 remainder
print(pow(4,2))#returns 4power2 (base,exponent)
'''
print(round(5.345,2))#digits to be rounded off
