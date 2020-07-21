#Program to split the words from a list avoiding repetitions
fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print('File cannot be opened:', fname)
    quit()
stuff = list()
for line in fh :
    for word in line :
        word = word.split()
        word = line.rstrip()
        if word not in stuff :
            stuff.append(word)
stuff.sort()
print(stuff)