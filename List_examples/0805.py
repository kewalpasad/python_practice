file = input('what is th name of th file:') #file from user
try:
    newfile = open(file,'r') #check for file
except:
    print("File not found") #if file doen't exists
    exit() #exit the program

print(newfile.read())