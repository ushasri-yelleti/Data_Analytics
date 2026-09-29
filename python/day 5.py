eg:
    text = 'python'
    print(text[-1])

txt = 'python is a programming language'
print(txt[-15])
#len:
txt = 'python is a programming language'
print(len(txt))           '''len is a built in function used to get the no. of charachters present in the string'''

syntax: len(variable_name)
# slicing: obtaining the exact part we need.
syntax: variable_name[start:end]
eg:
txt = 'python is a programming language'
print(txt[12:])
print(txt[:23])
print(txt[12:13])

#lower to uppercase: used to convert all the lower cases into upper cases
txt = 'python is a programming language'
print(txt.upper())


#upper to lower: used to convert all caps to lower. eg:
txt = 'python is a programming language'
print(txt.lower())

#indexing: used to know the index position of a charachter.  ''index()''. eg:
txt = 'python is a programming language'
print(txt.index('i'))
print(txt.index[7])

syntax: variable_name.index('substring',start,end)
eg: txt = 'python is a programming language'
print(txt.index('i',9,18))

#replace: used to replace the old substring with new substring
syntax: variable_name.replace(old,new)
eg: txt = 'python is a programming language'
print(txt.replace('python','java'))

#split: used to separate string based on the given substring
syntax: variable_name.split(substring)
eg: txt = 'python is a programming language'
print(txt.split(''))

#count: used to count the no. of occurences of each charachter  of  a substring
syntax: variable_name.count('substring')
eg: txt = 'python is a programming language'
print(txt.count('a',1,:12))
