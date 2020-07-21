#Program that finds the most common sender on a mail list
name = input('Enter file name: ')
count = 0
ddd = dict()
maill = list()
try :
    handle = open(name)
except :
    print('File cannot be opened: ', name)
    quit()
for line in handle :
    if not line.startswith('From') :
        continue
    words = line.split()
    maill.append(words[1])
for word in maill :
    ddd[word] = ddd.get(word, 0) +1
bigsender = None
bigcount = None
for sender, count in ddd.items() :
    if bigcount is None or count > bigcount :
        bigsender = sender
        bigcount = count
print(bigsender, bigcount)
