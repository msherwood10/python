import re
file = raw_input("Enter file:")
fhand = open(file)
numlist = list()
for line in fhand:
  line = line.rstrip()
  x = re.findall('[0-9]+', line)
  if not x:
      continue
  x = [int(i) for i in x]
  numlist.extend(x)

numcount = len(numlist)
numsum = sum(numlist)
print numcount, numsum
