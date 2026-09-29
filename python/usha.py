'''
module is a pythone file (.py)containing usable logic

import psclass10
#print(dir(psclass10))
#print(type(psclass10.data))
#print(type(psclass10.details))
print(psclass10.data)
print(psclass10.details("codegnan","vizag"))
#in above cases wer accesing via module name

#frm keyword helps us to get read methods/attributes

import psclass10
from psclass10 import data
print(data)
print(data.keys())

data['marks']=[45,35,25,15]
print(data)

print(psclass10.__doc__)#it returns docstring
'''
import psclass10
from psclass10 import *
print(data)
print(details('usha','viz'))

