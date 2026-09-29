'''
#scope of variables:--
1.local variable
2. global variable

1.local variable:-- A variable defined inside the function call is called loc var; where the variable can only be accessed within tht function.
ex:-
def display():
    name = 'usha'
    print(name)
display()
2. global variable:-- A variable defined outside the function call nd can be accessed anywhere throughout the program.
ex:--
a = 90
print(a)
def display():
    global a
    a = 10
display()
print(a)
# Global keyword: It is a keyword used to reaccess new values to variable tht was already defined outside the function call.
ex:
num = 7
def even_odd(num):
    if num % 2 == 0:
       print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(189)
#recursive function: the function will call itself until the base condition is met.
ex:--
'''
def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(5))

























    
























.
