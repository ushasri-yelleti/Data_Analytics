'''
#pattern printing
for <temp> in range(obj):
    statements(s)...

nested loops:--> (for in for) --> these r primarily used for pattern printing, matrix operations nd prblm solving scenarios
syntax:-->
for i in range(outer_loop_range):
    for j in range(inner_loop_range):#inner loop will be executed fr evry outer loop
    # code block
examples:--  
for i in range(3):# i=0,1,2
    for j in range(2):#j=0,1
        print(f'i={i},j={j}')

for i in range(3):
    for j in range(3):
        print(i,j)
      
for i in range(3):
    for j in range(3):
        print(i,j,end=' ')# by using end' ' entire result will be in a single line

for i in range(3):
    for j in range(3):
        print(i,j,end=' ')
        print("python")
    print('codegnan')    

for i in range(3):
    for j in range(3):
        print(i,j,end=' ')
        print("python")
        print('codegnan')  

for i in range(2):
    for j in range(i):
        print(f'i={i},j={j}')

for i in range(3):
    for j in range(i+1):
        print(f'i={i},j={j}')
        
for i in range(3):
    for j in range(i-1):# here if i=0; j becomes -ve,if i=1;j becomes 1 
        print(f'i={i},j={j}')
   
for i in range(3):
    for j in range(3):# here if i=0; j becomes -ve,if i=1;j becomes 1 
        print('*',end=" ")

for i in range(3):
    for j in range(3):# here if i=0; j becomes -ve,if i=1;j becomes 1 
        print('*',end=" ")
    print()

for i in range(3):
    for j in range(3):# here if i=0; j becomes -ve,if i=1;j becomes 1 
        print('*',end='')
    print()

for i in range(3):
    for j in range(4):# here if i=0; j becomes -ve,if i=1;j becomes 1 
        print('*',end=" ")
    print()

#number based patterns:--
for i in range(3):
    for j in range(4):# here if i=0; j becomes -ve,if i=1;j becomes 1 
        print(j+1,end=' ')
    print()

for i in range(1,4):
    for j in range(1,5):# here if i=0; j becomes -ve,if i=1;j becomes 1 
        print(j,end=" ")
    print()

for i in range(1,5):
    for j in range(1,5):# here if i=0; j becomes -ve,if i=1;j becomes 1 
        print(i,end=" ")
    print()

num=1  #for no.grid
for i in range(3):
    for j in range(3):# here if i=0; j becomes -ve,if i=1;j becomes 1 
        print(num,end=" ")
        num+=1
    print()

for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
        print()

rows = 5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end='')
    for j in range(i):
        print('*',end=' ')
    print()

num=1# print nos in right angle triangle
for i in range(4):
    for j in range(i+1):
        print(num,end=' ')
        num=num+1
    print()

char=65
for i in range(4):
    for j in range(i+1):
        print(chr(char),end=' ')
        char=char+1 
    print()

char=65
for i in range(4):
    for j in range(i+1):
        print(chr(65+i),end=' ')
    print()
'''
num=1
for i in range(4):
    for j in range(i+1):
        print(num+i,end=' ')
    print()
