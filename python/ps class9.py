'''
#accepting input frm user nd find even or odd
n = int(input("enter a no."))
result = lambda n: "even" if n%2==0 else "odd"
result1 = lambda n: n**2 if n%2==0 else n**3
print(result(n))
print("new result is", result1(n))

names=['codegnan','python','usha','data','java']
g= lambda x:x in names
h= lambda x:len(x) in names
o= lambda x:len(x)
print(g('python'))
print(h('codegnan'))
print(o('usha'))

#filter(), map(), reduce()
#filter()--> we want specific filtered result
data=[1,3,4,5,24,12,36,3]
#filter only even no.s frm list
new_data= list(filter(lambda x:x%2==0,data))
print(new_data)

#same prgrm but with using user defined func nd for loop
def filter_even(data):
    new_data=[]
    for x in data:
        if x%2==0:
           new_data.append(x)
    return new_data
data=[1,3,4,5,24,12,36,3]
result=filter_even(data)
print(result)

#filter desired names frm list
names=['usha','python','sri','java','sql']
new_names=list(filter(lambda i:len(i)>=6,names))
print(new_names)

#map()--> it will apply logic fr each value(google maps)
lst=list(map(int,input("enter the values").split(',')))
print(lst)
data=[1,3,5,7,-23]
print(data)
final=list(map(lambda x,y:x+y,lst,data))#it automatically maps the length
print(final)

#prices
prices=[2000,2500,1500,4500,3000]
#discount of 10% for every price
disc_prices=list(map(lambda price:(price-price*0.1),prices))
print(disc_prices)

#reduce--> functools
#reduce--> it will check fr logic nd make it to a single value
import functools
from functools import reduce
result=reduce(lambda x,y:x*y,[12,3,4,5,6])
print(result)
f=reduce(lambda x,y:x+y,[12,3,4,5,6])
print(f)

#task--> above 2 use cases using functions

#recursive functions--> a function which calls itself
#factorial,fibonacci,sum of nos...
#recursive function--> basecase(it tells when to stop the recursion)
                       recursive case(it tells how to start recursion)
Syntax:
def func():
    """docstring"""
    if base: #base case
         return
    func()#recursive case
func()

#factorial
#5!--> 5*(5-1)*(5-2)*(5-3)*(5-4)*1
n=int(input("enter the value"))
def fact(n):
    """factorial"""
    if n==0 or n==1:
        return 1
    elif n<0:
        return"input must be greater than 1"
    else:
        return n*fact(n-1)
print(fact(n))

#functions r 1st class objects
#they can pass another func as arguement
#a func can return another func
#a func can be inside another func
#a func can call itself
