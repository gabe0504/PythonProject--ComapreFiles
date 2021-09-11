def printFiles():
    infile=open('correct.txt','r')
    line=infile.readline()
    lineList=[]
    while line !='':
        line=infile.readline()
        lineList.append(line)
    infile.close()
    infile2=open('myfile.txt','r')
    line2=infile2.readline()
    lineList2=[]
    while line2 !='':
        line2=infile2.readline()
        lineList2.append(line2)
    infile2.close()
    for x in range(len(lineList)):
        if lineList[x] == lineList2[x]:
            print('Line>', x+1 , '- same')
        elif lineList[x] != lineList2[x]:
            print('Line>', x+1, 'in myfile is different\n', '\n       CORRECT>>\n',
                  repr(lineList[x]), '\n       MYFILE>>\n', repr(lineList2[x]), '\n')
printFiles()
