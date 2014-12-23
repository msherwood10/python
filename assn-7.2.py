fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
		continue
    count = count+1
    spos = line.find(":")
    trunctext = line[spos+1:40]
    cleantext = trunctext.lstrip()
    numtext = float(cleantext)
    sum = sum+numtext
print "Average spam confidence:", sum/count