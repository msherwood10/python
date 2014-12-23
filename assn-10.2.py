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
hrdict = dict()
for line in fhand:
	line = line.rstrip()
	#ignore all lines except lines that start with "From"
	if not line.startswith("From "):
		continue
	timepos = line.find(":")
	#THIS IS BASICALLY HARDCODED AND TERRIBLE - FIX
	time = line[timepos-2:50]
	hour = time.lstrip().split(":")
	#hour is the first entry in the new list
	hour = hours[0]
	#adds the hour to the list if it is not already present and adds 1 for the count
	hrdict[hour] = hrdict.get(hour, 0) + 1
#now create a list to store the tuples (hour and count of hour)
lst = list()
for key, val in hrdict.items():
	lst.append((key, val))
#sort the tuples by hour from highest to lowest
lst.sort()
#and print out the list = done!
for key, val in lst[:]:
	print key, val