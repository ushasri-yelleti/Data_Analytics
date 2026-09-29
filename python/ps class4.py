#exception
'''
try:
    a,b = map(int,input("enter the values").split(','))
    result = a/b
    print(result)
except exception as e:
    print("find it")
    print(e)
#possible errors--> TypeError, NameError, ValueError, Indexerror, Zero divisionError, attribute Error, Arithmetic error
try:
    a,b = map(int,input("enter the values").split(','))
    result = a/b
    print(result)
except ValueError:
    print("enter only integers")
except ZeroDivisionError:
    print("make sure to give denominator greter than 0")
except NameError:
    print("understand the syntax nd avoid spelling mistakes")
except AttributeError:
    print(" chck the method names nd functions properly")
finally:
    print("end of the handling")
'''
#multiple exceptions at a time
try:
    a= [12,3,4,5]
    print (a[0])
    a.append('codegnan')
    print(a)
except(IndexError,NameError,AttributeError)as e:
    print(e)
finally:
    print("done")
    

