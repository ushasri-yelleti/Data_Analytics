'''
batch = ['usha','sri','latha','teju','python','pooji','java']
batch.insert(2,("vizag","hyd","vijayawada"))
print(batch)
print(len(batch[2]))
print(batch[2][:2]) #sub indexing
print(batch[2][1])
print(batch[2][::2])
print(batch[2].index('hyd'))# it returns the index value of hyd
#index-- first occurence
#count-- returns the count of objects
print(batch[2].count('codegnan'))#index will raise an error whereas count will return 0 as this element is not present in the tuple
batch.insert(3,["pfs","da","jfs"])
print(batch)
print(batch[3])
print(batch[3][1])
batch[3][2] = batch[3][2].upper()
print(batch[3][2])
batch[3].append('AAA')
print(batch[3])
print(len(batch))
print(batch)
batch.remove('java')#used to remove the element  
print(batch)
#remove is used to remove the value nd pop is used to remove values through their index
batch.pop()# if we dont give the index position, by default its gonna delete the last element
print(batch)
batch.pop(6)#removes the value at index 6
print(batch)
#batch[2].remove('hyd')-- it raises an attribute error
#tuple is immutable, we cant insert/remove elements in it
#if we want to remove the entire data, by keeping the list same, then we use-- clear()
batch.clear()
print(batch)

#dictionaries
#it is a combination of key value pairs nd the keys must be unique
#keys can be int,float,string,list
'''
details = {}
print(len(details))
details['batch'] = ['da6']
print(details)
details['course'] = ['python']
print(len(details))
print(details)
details['students'] = ['usha','sri']
print(len(details))
print(details)
# if we want to update the dict at once--
details.update({'branch':('hyd','vizag'),'subjects':{'python','aptitude','softskills'}})
print(details)
print(len(details))
#keys(),values(),items()
print(details.keys())#returns only keys
print(details['batch'])
details['batch'].extend(['jfs','pfs'])#used to add values to keys
print(details)
details['subjects'].add('dsa') #set is unique nd unordered.
print(details)
#task--> details -->list,set,dictionary(use codegnan portal as ex)
#exams,mock interviews,project demos

