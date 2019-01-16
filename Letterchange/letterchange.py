newstring = ''
string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ5"
for letter in string:
    if letter>='a' and letter <='y':
        newletter = chr(ord(letter)+1)
        #print("atoy",newletter)
    elif letter == 'z':
        newletter = 'a'
        #print("a")
    elif letter >='A' and letter <= 'Y':
        newletter = chr(ord(letter)+1)
        #print ("AtoY",letter)
    elif letter == 'Z':
        newletter = 'A'
        #print("A")
    newletter = letter
    newstring+=newletter
print(newstring)