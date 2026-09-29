Arguments:--
1. Positional arguments:-- the arguements should be same at def line and calling, incase if they are not same no., it will raise an error
syntax: def add_(a,b):
            print(a+b)
        add_(a:5,b:7)
eg:--
num = 0
num_2 = 1
def feb_(a,b):
    print(num,num_2,end='')
    for i in range(1,10):
        num_3 = num+num_2
        num = num_2
        num_2 = num_3
        print(num_3,end='')
feb_(num,num_2)
2. Default arguements:-- the arguements where the function will only consider the data at calling, even though data is present at def line
syntax: def feb_(num,num_2):
            print(num+num_2)
feb_(num:[1,3],num_2:[5,6])
eg:--
def data_(a=8,b=9):
    print(a+b)
data_(a:1,b:2)
eg:--
def prime(num=10,count=1):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
prime(num = int(input("enter a no.:")),count=0)

3. keyword arguements:-- they send arguements in a pair(a=2), nd the passing order is not considered
eg:--
def data_(age,name,batch,loc):
    print(name)
    print(age)
    print(batch)
    print(loc)
data_(name='usha',age=22,batch=6,loc='viz')
4. variable length arguements:-- adding a (* call it as args) before a variable at parameters, we can pass a tuple of arguements and can be accessed with indexing
eg:--
def all_(*name):
    print(name[1])
all_(*name:'usha','sri','sony', 'sai')
5. keyword length arguement:-- 
eg:--
def details(**data_):
    print(data_.keys())
details(name='usha',age=22,batch=6, loc='viz')
6. return keyword:-- its used inside the function, once the return is executed, it means it'll get back to calling with return values
eg:--
def all_(a,b):
    return a-b
print(all_(7,9))

