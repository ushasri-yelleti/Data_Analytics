'''while true:
     try:
         weight = int(input("enter the weight in kgs:"))
         height = float(input("enter the height in kgs:"))
         if weight > 0 and height > 0:
             break
        else:
            print
#File handling--> create files, make some chnages over fiels
#we will use open(),with()--->.txt files
file = open('Project name--ATM.txt','r')
#to read content frm the files
print(file.read())
print(file.readline())  #reads a single line frm the file    
print(file.readlines())#returns list of lines
# w mode--> it automatically creates a new line nd if same file is existing
#it overrides
file = open('proje
print(file)#print(file.read()) is not readable

file.write("pfs and da6 students r good")
file.close()#once the file is closed, then only the data is written into the file
with open('usha.txt','w')as file:
file.write("pfs nd da6 students r improving")
file.write("yes they r gud bt sometimes mischevious")
file.write("\n but they follow wht we say")
with open('usha.txt','a') as f:
    f.write("\n 2dy we r having a webinar related to voice ai agent")
'''
with open('usha.txt','r+') as f:
     print(f.read())
           
