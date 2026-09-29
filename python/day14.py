words_ = input("enter a word:")
vowels = 'aeiouAEIOU'
count = 0
for i in words_:
    if i in vowels:
        count += 1
        print(f'{i} is vowel')
print(count)
#count no.of consonants in a word using operator:--
words_ = input("enter a word:")
vowels = 'aeiouAEIOU'
count = 0
for i in words_.upper:
    if i not in vowels:
        count += 1
        print(f'{i} is consonant')
print(count)
#remove duplicates from a list:--
digits_ = [1,2,3,1,5,3]
empty_ = []
for i in digits_:
    if i not in empty_:
        empty_.append(i)
print(empty_)
#find out the duplicate values in tuple:--
#
words_= 'python is a lanaguage'
for i in words_:
    if i == ' ':
        
        



