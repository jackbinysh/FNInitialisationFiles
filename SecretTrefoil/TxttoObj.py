
name = "Seven6"

TheFile = open(name+".txt","r")
Lines = TheFile.readlines()
datalength = len(Lines)

for (i,line) in enumerate(Lines):
    # strip off newline
    filteredline = line.split('\n')[0]
    # add a v
    filteredline = "v "+filteredline
    Lines[i] = filteredline

# okay now add the edge data

for i in range(1,datalength):
    Lines.append("l "+ str(i)+ " " + str(i) +" "+ str(i+1))

Lines.append("l "+str(datalength)+ " " + str(datalength) +" "+ str(1))

# write the vertex list to file
outputfile = open(name+".obj", "w")

for line in Lines: 
    outputfile.write(line)
    outputfile.write("\n")
outputfile.close();

