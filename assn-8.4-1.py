#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#
#fname = raw_input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#print line.rstrip()
#Opens a file, splits each line in the file into a list of words, builds a list of all of the unique words in the file (i.e. does not count the same word multiple times); end result is a list of all of the words in the file sorted from A-Z.  

fname = raw_input("Enter file name: ")
fhand = open(fname)
lst = list()
for line in fhand:
	line = line.rstrip()
	words = line.split()
	for w in words:
		if not w in lst:
			lst.append(w)
lst.sort()
print lst