name = input('what is the name of th file:') #file from user
try:
    file = open(name,'r') #check for file
except:
    print("File not found") #if file doen't exists
    exit() #exit the program
count = 0
for line in file:
    if line.startswith('From ')==True:
        email = line.split()
        email = email[1]
        print(email)
        count+=1

print("There are %d lines in the file with From as the first word"%(count))