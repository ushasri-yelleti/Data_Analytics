#update:-- method is used to update a key, incase if the key is not present inside the dictionary then it will add tht key:value
syntax: dict.update({key:value})
eg: print(data_)
data_['AC'] = 12345676548
data_.update({'name':'usha'})
print(data_)
** there is another way to update a key
syntax: dict[key] = value
eg:
data_ = {'name':'usha',
         'balance':7000,
         'adr':5627282926829,
         'PANC':'GFP789GY768',
         }
print(data_)
data_['AC'] = 12345676548
data_.update({'name':'usha'})
data_.update({'ATMPIN':56783})
print(data_)
#values():-- it is used to get all the values frm the dict
syntax: (dict.keys())
data_ = {'name':'usha',
         'balance':7000,
         'adr':5627282926829,
         'PANC':'GFP789GY768',
         }
print(data_.values())
#keys():-- it is used to get all the keys from the dict
syntax: dict.keys()
eg: data_ = {'name':'usha',
            'balance':7000,
            'adr':5627282926829,
            'PANC':'GFP789GY768',
         }
print(data_.keys())
#items():-- this method will get the key:value separted frm the dict
syntax: dict.items()
eg: data_ = {'name':'usha',
             'balance':7000,
             'adr':5627282926829,
             'PANC':'GFP789GY768',
             }
print(data_.items())
#clear():-- used to delete entire data frm dictionary
syntax: dict.clear()
data_ = {'name':'usha',
         'balance':7000,
         'adr':5627282926829,
         'PANC':'GFP789GY768',
         }
print(data_)
data_.clear()
print(data_)
#del():--
data_ = {'name':'usha',
         'balance':7000,
         'adr':5627282926829,
         'PANC':'GFP789GY768',
         }
print(data_)
del data_['adr']
print(data_)
data_.clear()
print(data_)

#statements:--
**3 types:--> condition, looping,control statements
condition satements:if, if else
IF: if the condition becomes true only then it will execute inside the block of code, incase if it becomes false then it will never enter inside the block  
eg:
    a=78
    b=67
    if a>b:
        print(a)
if-else: fallback statements/ incase if condition will be false else block will be executed
eg:
age = 15
if age >= 18:
    print (f'your {age} eligible to vote')
else:
    print(f'your {age} you have to wait{18-age}')

a = 90
b = 895
if a>b:
    print('a is greater')
else:
    print('b is greater')
    








