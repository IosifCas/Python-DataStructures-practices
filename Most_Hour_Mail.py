#Program that reads the hour a mail was sent and prints them in order
name = input('Enter file name: ')
count = 0
ddd = dict()
maill = list()
nlist = list()
try :
    handle = open(name)
except :
    print('File cannot be opened: ', name)
    quit()

for line in handle :
    if not line.startswith('From ') :
        continue
    hours = line.split()
    maill.append(hours[5])

for hour in maill :
    endpos = hour.find(':')
    xhour = hour[:endpos]
    ddd[xhour] = ddd.get(xhour, 0) +1

for k, v in ddd.items() :
    ntup = (k,v)
    nlist.append(ntup)

print(nlist)
nlist = sorted(nlist,)
for k, v in nlist :
    print(k,v)