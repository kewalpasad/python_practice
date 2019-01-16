def LetterChanges(string):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    newstring = []
    string = string.lower()
    for letter in string:
        if letter in alpha:
            if letter is 'z':
                newstring.append('A')
            elif alpha[alpha.index(letter)+1] in 'aeiou':
                newstring.append(alpha[alpha.index(letter)+1].upper())
            else:
                newstring.append(alpha[alpha.index(letter)+1])
        else:
            newstring.append(letter)
    newstring =''.join(newstring)       
    return newstring  
    
print(LetterChanges("AbcdeFghiJklmnOpqrstuvwxyz5"))