def printFiles():
    infile=open('myfile.txt','r')
    line=infile.readline()
    lineList=[]
    while line !='':
        print(line)
        line=infile.readline()
        lineList.append(line)
    infile.close()
    infile2=open('correct.txt','r')
    line2=infile2.readline()
    lineList2=[]
    while line2 !='':
        print(line2)
        line2=infile2.readline()
        lineList2.append(line2)
    infile2.close()
    if lineList in lineList2:
        print("True")
    else:
        print("False")
printFiles()
