#for loop:-- it is used to iterate over a sequence or iterable datatypes
eg: nums = [12,3,5,78]
for num in nums:
    print(num)
#else in for:-- unlike if else, else block in for statement is executed after completion of all interactions
eg: nums = 'python'
for num in nums:
    print(num)
else:
    print('for ended')

nums = [1,2,3,4,5,8,9]
for num in nums:
    print(num)
    if num == 3:
        break

val_ = [1,2,3,4,5,8,9]
for j in val_:
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')
#break statement:-- the break statement is used to stop the interaction based on the condition given
#continue statement:-- the continue statement is a keyword used to skip the current iteration based on the condition
eg: nums = [1,2,3,4,5,8,9]
for num in nums:
    if num == 5:
        continue
    print(num)
#pass:-- it is called as a space holder, tht is used after statements like (if, for, else) not to raise any error
eg: for j in range(1,11):
    if j == 15:
        print(j)
    else:
        pass
#assert:-- it is a keyword used to check the condition, incase the condition is false, it will raise the error(assertion error) 
eg: age = 15
assert age >= 18, 'not eligible to vote'
print('ur eligible to vote')

**while loop**
eg: num = 1
while num < 5: #1 <5
    print(num)
    num += 1

1. find out a no. is even or odd
2. remove duplicates frm list
3. armstrong no.
4. no. of vowels in the string
5. count the words in a string


m






















        
