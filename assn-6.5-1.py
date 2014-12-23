#Program looks for a specific value in a string using ":" as a reference; this program is built to search through files that are not "clean" / unstructured, ignoring irrelevant words, spaces, breaks, etc.
#text = "X-DSPAM-Confidence:    0.8475";

text = "X-DSPAM-Confidence:    0.8475";
spos = text.find(":")
trunctext = text[spos+1:40]
cleantext = trunctext.lstrip()
numtext = float(cleantext)
print numtext
