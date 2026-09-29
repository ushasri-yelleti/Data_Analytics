'''
#list comprehension:- it is a shorter form of syntax to create a list
old_ = (9,5,9,8,5)
new_ = [i for i in old_]
print(new_)

 old_ =('python;)
new_ = [i for i in old_]
print(new_)
 syntax1:-- [expression loop condition]
 syntax2: [expression condition else loop]
eg>=
any_ = [ for i in range(1,6)for j in range(1,10)]

of = [[1,2,3],
      [3,7,8],
      [5,7,2]]
data_ = [num for i in of for num in i]
print(data_)
#nested comprehension:-- using list comprehension generating list inside list
any_ = [[i*j for i in range(1,6)]for j in range(1,10)]
print(any_)

of = [[1,2,3],
      [3,7,8],
      [5,7,2]]
data_ = [num for i in of for num in i]
print(data_)
#generator:-- a generator is a spcl function which generates one value at a time
'''
def all_():
    for j in range(1,10):
        yield j
j = all_()
print(next(j))


