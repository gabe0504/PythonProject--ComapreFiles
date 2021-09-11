#main() function pulls tw0 files into program and assigns them to variables for later comparison
def main():
    infile=open('correct.txt','r') #assigns correct.txt to variable infile.
    line=infile.readline()         #readline method allows contents to be read and assigned to line variable
    correctfile=[]                 #empty list named correctfile will receive the contents of correct.txt
    while line !='':               #conditional loop assigns lines to list while there are no empty lines.
        line=infile.readline()
        correctfile.append(line)
    infile.close()
    infile2=open('myfile.txt','r') #same process as lines 3-5, but for second file called myfile.txt.
    line2=infile2.readline()
    myfile=[]
    while line2 !='':              #same process as lines 6-8, but for second file called myfile.txt.
        line2=infile2.readline()
        myfile.append(line2)
    infile2.close()
    filecompare(myfile, correctfile)#variable called to compare files, and both files passed as arguments.

def filecompare(myfile,correctfile):     #variable defined.
    for x in range(len(correctfile)):    #for loop iterates over each element in the file
        if correctfile[x] == myfile[x]:  #if statment prints that files are the same at line #x
            print(' Line>\t', x+1 , '- same')
        elif correctfile[x] != myfile[x]:#elif statements prints if lines differ and how they differ.
            print(f' Line>\t', x+1, 'in myfile is different\n', '\n\tCORRECT>>\n',
                [correctfile[x]], '\n\tMYFILE>>\n', [myfile[x]]) #formatted to print as list
main()                                   #this program prints out the newline character to demonstrate
                                         #the files have different spacing and different sums.
