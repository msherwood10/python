#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.

#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)

file = raw_input("Enter file:")
if len(file) < 1 : name = "mbox-short.txt"
fhand = open(file)
relIDdict = dict()
IDcount = 0
for line in fhand:
	line = line.rstrip()
	line = line.strip()
	#ignore all lines except lines that start with "1"
	if not line.startswith('"1'):
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
#sort the tuples by hour from highest to lowest
lst.sort()
#and print out the list = done!
for key, val in lst[:]:
	print key, val
print 'There are', IDcount, 'unique RelationshipIDs in this file.'
