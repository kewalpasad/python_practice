#take input numbers from the user and find the min and max number
numberlist = [] #declaring a list variable
number = '' #declarinf a number variable
while number != "done": #if done then exit
    number = input("Enter a number:")
    if number != 'done': #if done then do not convert it to float
        number = float(number)
        numberlist.append(number) #add the new number to the list

print("Minimum:",min(numberlist)) #print the minimum number
print("Maximum:",max(numberlist))#print the maximum number