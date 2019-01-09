# count the email from all the senders
with open("mbox-short.txt",'r')as file: #open file 
    emailList = {} #def as dict{}
    for line in file:
       if line.startswith("From ") == True: #take line starting with From
           line = line.split()
           email = line[1] #take out the email component
           emailList[email] = emailList.get(email,0)+1 #count the email companents 

print(emailList) #display the the dictory of emails and their count of occurence.