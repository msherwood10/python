fname = raw_input("Enter file name: ")
fhand = open(fname)
lst = list()
counts = dict()
for line in fhand:
	line = line.rstrip()
	for line in fhand:
		spos = line.rfind("-")
		trunctext = line[spos +2:100]
		#debugging
		#print trunctext
		author = trunctext.lstrip()
		counts[author] = counts.get(author, 0) +1
		if not author in lst:
			lst.append(author)
lst.sort()
#debugging
#print lst
#for key, val in counts.items():
#	print key, val
with open('authorlist.txt', 'w') as f:
	for item in lst:
		authorstring = str(item)
		#debugging
		#print authorstring
		f.write(authorstring)