#count the number of emails send on days of the week
with open("mbox-short.txt",'r')as file: #read the file
    count = {} #def data as a dict()
    for line in file:
        if line.startswith('From ') == True: #only lines with From at the start
            line = line.split()
            day = line[2] # only take the day info
            count[day]=count.get(day,0) +1 #add or increment the value of the day count

print(count)