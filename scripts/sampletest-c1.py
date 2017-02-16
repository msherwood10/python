#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.

#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)

file = raw_input("Enter file:")
if len(file) < 1 : name = "sampletest_c2.txt"
fhand = open(file)
relIDdict = dict()
IDcount = 0
badcount = -1 #set to -1 because I haven't figured out how to escape the header row yet
for line in fhand:
	line = line.strip()
	#ignore all lines except lines that start with "1
	if not line.startswith('"1'):
		badcount = badcount + 1
		continue
	splitline = line.split("|")
	relID = splitline[37]
	#adds the hour to the list if it is not already present and adds 1 for the count
	relIDdict[relID] = relIDdict.get(relID, 0) + 1
	IDcount = IDcount + 1
#now create a list to store the tuples (relID and count of relID)
lst = list()
for key, val in relIDdict.items():
	lst.append((key, val))

with open('output.txt', 'w') as f:
	f.write('\n'.join('"%s | "%s' % x for x in lst))
	#deprecated code
	#for key, val in lst[:]:
	#	relIDstring = str(key)
	#	f.write(relIDstring, val)

print badcount, 'bad lines were ignored'
print 'There are', IDcount, 'total RelationshipIDs in this file.'
print len(lst), 'of them are unique.'