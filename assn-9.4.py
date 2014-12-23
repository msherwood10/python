#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)

name = raw_input("Enter file:")
fhand = open(name)

emails = list()
counts = dict()

for line in fhand:
	line = line.rstrip()
	if not line.startswith("From "):
		continue
	words = line.split()
	emails.append(words[1])

for sender in emails:
	counts[sender] = counts.get(sender,0) + 1

bigcount = None
bigword = None

for sender,counts in counts.items():
	if bigcount is None or counts > bigcount:
		bigword = sender
		bigcount = counts

print bigword, bigcount