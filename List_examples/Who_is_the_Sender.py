name = input('what is the name of th file:') #file from user
try:
    file = open(name,'r') #check for file
except:
    print("File not found") #if file doen't exists
    exit() #exit the program
count = 0
for line in file:
    if line.startswith('From ')==True: #if line starts with From
        email = line.split() #split each word
        email = email[1] #take 2nd word
        print(email) # print the senders name
        count+=1 #increment the counter for each sender

print("There are %d lines in the file with From as the first word"%(count))