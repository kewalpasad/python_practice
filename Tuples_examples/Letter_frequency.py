with open("words.txt",'r') as file:
    wordcount = {} #def dict()
    length = 0 #to know the numbers of letters
    for line in file:
        line = line.rstrip() # removed the \n
        line = line.lower() #all lover case
        for letter in line:

            if letter >= 'a' and letter <= 'z': #only allow a to z

                length += len(letter) #count the number of letters

                wordcount[letter] = wordcount.get(letter,0)+1 # add or increment the value of key
wordlist = list()
for k,v in wordcount.items():
    wordcount[k] = (v/length*100) #find the % or frequency

for k,v in wordcount.items(): #convert dict to list
    wordlist.append((k,v))
    wordlist.sort() #sort aplhabetically

for k,v in wordlist: 
    print("%s %0.2f"%(k,v)) # print with value in 2 decimal floating point