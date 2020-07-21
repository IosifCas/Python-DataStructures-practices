#Program that prompts the user for the name of a file and prints the contents of the file in upper case
fname = input('Enter file name: ')
try :
    fh = open(fname)
except :
    print('File cannot be opened:', fname)
    quit()
for line in fh :
    line = line.rstrip()
    line = line.upper()
    print(line)