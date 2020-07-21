#Program that computes the average of SPAM confidence
fname = input('Enter file name: ')
count = 0
try :
    fh = open(fname)
except :
    print('File cannot be opened: ', fname)
    quit()
for line in fh :
    if not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split()
    print(words[1])
    count = count +1
print('There were', count, 'lines in the file with From as the first word')