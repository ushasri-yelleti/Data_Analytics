'''
a = 15
b = 25
print(a+b)
'''
batch = ['pfs6','da6']
print(batch)
print(type(batch))
print(len(batch))
# idle is color coding editor (violet- builtin functions
#to add more elements in list we use-- append()-adds element to the end of the list,extend(),insert()
batch.append('usha')
print(batch)
batch.append(['sri','latha'])
print(batch)
#one list is another list is known as nested list
batch.extend(['sri','latha'])
print(batch)
batch.insert(0,'teju')
print(batch)
batch.insert(-1,'python')
print(batch)
print(len(batch))
#indexing:--[]--> index starts at 0 nd ends at len(obj)-1
print(batch[0])#to get the element stored in the index position
#print(batch[34])# gives an "index error" becoz the length is only 8 nd we r accessing extra
#slicing:-- to access grp of values[start:end]-- start is included,end is excluded
print(batch[0:3])
print(batch[4:])
#last 3 elements--> we prefer negetive index values
print(batch[-3:])
#first 3 elements:--
print(batch[:3])
#striding--> [start:end:step] (step count starts frm 2(if we give 1 all values will be displayed))
print(batch[::3])#(3-1=2 (so, it subsequently skips 2 elements in btw nd displays output))
print(batch[1:5:2])# first performs batch[1:5] then skips 1 element in btw
#tryout
print(batch[:7:4])
print(batch[7::4])
print(batch[1::5])
print(batch[1:7:-2])
print(batch[-1:-4:-1])

