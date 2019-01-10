#extract the hour detail and count numbers of times it is repeated also sort them in alphabetical order
with open("mbox-short.txt",'r') as file:
    hourcount = {}
    for line in file:
        if line.startswith("From ") == True: #consider only if line starts with From
            line = line.split()
            time = line[5] #take out the time details from the line
            hour, minutes, seconds = time.split(':') # split the line to get hour, minutes and seconds info
            hourcount[hour]= hourcount.get(hour,0) + 1 # add or increment the hourcount value

hourlist = list() #converting dict to tuples
for key, value in hourcount.items():
    hourlist.append((key,value))
    hourlist.sort()
    
for k,v in hourlist:# to print each key and value in each line
    print (k,v)
