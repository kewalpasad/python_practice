#scan a text and then make a dictory of all the words and assigning there count to it
with open("words.txt",'r')as file: #with also does execptional handling and closes the file automatically
    wordlist = {} # defining the dict()
    for line in file:
        words = line.split()
        for word in words: #iterating through each word in the line
            wordlist[word] = wordlist.get(word,0) + 1 #checks for the word if not found then gives a default value 0 if found then incremeants the value of word
                                                    #replaces #if word not in wordlist:
                                                                    #  wordlist[word] = 1
                                                                #else:
                                                                    #wordlist[word] = wordlist[word] + 1

print(wordlist['is'])
print(wordlist.get('the',0)) # checkig for the word and is not found will return 0 instead of error