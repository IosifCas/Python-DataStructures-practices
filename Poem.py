#Second attempt to slice the poem
fname = input('Enter file name: ')
try :
    fh = open(fname)
except :
    print('File', fname, 'cannot be opened:')
    quit()
l = list(fh)
fl = list()
for line in l :
    line = line.rstrip()
    l2 = line.split()
    for word in l2 :
        word = word.rstrip()
        if word in fl : continue
        fl.append(word)
        #print(word)
fl.sort()
print(fl)
