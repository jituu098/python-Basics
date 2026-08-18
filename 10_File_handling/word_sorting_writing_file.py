infile = open("poem.txt","r")
outfile = open("resultpoem.txt","w")
words =[ ]
for line in infile.readlines():
    line = line.strip().split()
    for i in line:
        words.append(i)
infile.close()
words.sort()
le = len(words)
for i in words:
    outfile.write(i)
    outfile.write("\n")

outfile.write(f"The number of words is {le}")
outfile.close()