numlist = ['1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10 ']
a = dict()
count = -1
line_count = -1
with open('BR720.txt') as file:
	for line in file:
		line = line.rstrip()
		line_count = line_count +1
		if any(num in line for num in numlist):
			count = count +1
print count
print line_count
#			numlist[num] = numlist.get(num, 0) + 1
#lst = list()
#for key, val in numlist.items():
#	lst.append((key, val))
