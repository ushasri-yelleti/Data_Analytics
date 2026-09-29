#Tuple: It is a collection of different datatypes that r separated by, nd represented by(). It is immutable nd we can pass a tuple value tht can be assigned to variables but should match same no. of variables and values inside the tuple.
Eg:t = (1,'python',[3,4],(7,9))
print(len(t))

name,age= ('usha',34)
print(name)
print(age)

#print max value: max()-- used to find out the max value frm the tuple.Eg:-
so = (67,5,89,61)
print(max(so))
#print min value: min()-- used to find out the least value frm the tuple. Eg:-
so = (67,5,89,61)
print(min(so))
#count: used to count an item present in the tuple.(also give how many time a value is repeated in the tuple)Eg:-
so = (67,5,89,5)
print(so.count(5))
#concatenation(+): used to join or add 2 tuples. Eg:-
so = (5,96,87,7)
do = (51,24)
print(so+do)

#SETS:-- 


#union:-- the union() will combine 2 sets into a single set.
Syntax: set_1.union(set_2) or set_1 | set_2
eg: data_ = {1,2,3,4}
nums = {4,5,6}
print(data_.union(nums))
print(data_ | nums)
#intersection:-- this will give us the common elements frm both the sets.
Syntax: set_1.intersection(set_2) or set



#difference:-- it will display different elements frm set_1 but not the set_2 elements
syntax: set_1.difference(set-2) or set_1-set_2
eg: data_ = {1,2,3,4}
nums = {4,5,6}
print(nums - data_)
print(nums.difference(data_))
#symmetric difference:-- displays different elements frm both sets
syntax: set_1.symmeteric_difference(set_2) or set_1 ^ set_2
eg: data_ = {1,2,3,4}
nums = {3,4,5,6}
print(nums ^ data_)
print(data_.symmetric_difference(nums))
#set methods:--
#add():- this method will add only one element at a time
syntax: set.add(element)
eg: data_ = {1,2,3,4}
print(data_)
data_.add(7)
print(data_)
#updata:-- we can add more than one element by using update method
syntax: set.update([elements]) or set_1.update(set_2)
eg: data_ = {1,2,3,4}
nums = {4,5,6}
print(data_)
data_.update([8,9])
print(data_)
data_.update(nums)
print(data_)
#remove:-- it will delete the given element frm the set; if the element is not present in the set it will raise error
syntax: 
eg: data_ = {1,2,3,4}
data_.remove(3)
print(data_)
data_.remove(5)
#discard:-- this method is used to delete the elements but it never throws any error, even if the element is not in the set
eg: data_ = {1,2,3,4}
data_.discard(7)
print(data_)
data_.discard(1)
print(data_)
#clear:-- this method is used to delete all the elements frm the set nd it will return empty set
syntax: set.clear()
eg: data_ = {1,2,3,4}
print(data_)
data_.clear()
print(data_)
