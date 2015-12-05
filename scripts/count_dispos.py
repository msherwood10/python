file = raw_input("Enter file:")
fhand = open(file)
linecount = -1
dispolist = list()
dispodict = dict()
for line in fhand:
	line = line.rstrip()
	linecount = linecount + 1
	if linecount > 0:
		items = line.split("|")
		if items[0] is "Z":
			continue
		dispolist.append(items[4])

for dispo in dispolist:
	dispodict[dispo] = dispodict.get(dispo,0) +1

lst = list()
for key, val in dispodict.items():
	lst.append((key, val))
lst.sort()
print "Dispo","Count"
for key, val in lst[:]:
	print key, val
print "TOTAL",sum(dispodict.values())