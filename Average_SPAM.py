#Program that computes the average of SPAM confidence
fname = input("Enter file name: ")
count = 0
num = 0
try :
    fh = open(fname)
except :
    print('File cannot be opened: ', fname)
    quit()
for line in fh :
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    strtpos = line.find(':')
    extract = line[strtpos + 1 :]
    count = count +1
    n = float(extract)
    num = num + n
avg = num / count
print('Average spam confidence: ', avg)