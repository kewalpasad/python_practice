#
file = input('what is th name of th file:') #file from user
try:
    newfile = open(file,'r') #check for file
except:
    print("File not found") #if file doen't exists
    exit() #exit the program

wordlist = list()
for line in newfile: #iterating through lines
    line = line.rstrip() #removing /n from the file
    words = line.split() #splitting the line to words
    for word in words:
        if word not in wordlist:    
            wordlist.append(word) #if word not found the add that word into the list
wordlist.sort() #sort the list alphabetically
print(wordlist)