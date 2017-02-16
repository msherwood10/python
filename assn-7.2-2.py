# Use the file name mbox-short.txt as the file name
fname = "C:\Python27\mbox-short.txt"
fh = open(fname)
xspam = list()
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        zeropos = line.find("0")
        eol = line.find("\n")
        spamtext = line[zeropos:eol]
        spamval = float(spamtext)
        xspam.append(spamval)
        count = count + 1
xspamavg = sum(xspam)/count
print "Average spam confidence:",xspamavg