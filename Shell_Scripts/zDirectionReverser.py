name = "Eight6"

TheFile = open(name+".txt","r")
Lines = TheFile.readlines()

for (i,line) in enumerate(Lines):
    # strip off newline
    filteredline = line.split('\n')[0].split(" ")
    # reverse the z coordinate
    filteredline[2] = str(-float(filteredline[2]))
    Lines[i] = " ".join(filteredline)

# write the vertex list to file
outputfile = open(name+"_reversed_z_direction.txt", "w")

for line in Lines: 
    outputfile.write(line)
    outputfile.write("\n")
outputfile.close();

