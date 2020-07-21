#Program to find a value on a string, extract it, and print the value
text = 'X-DSPAM-Confidence:    0.8475'
strtpos = text.find('0')
stoppos = text.find('5')
host = text[strtpos : stoppos+1]
num = float(host)
print (num)
