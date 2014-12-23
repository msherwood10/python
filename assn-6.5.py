#text = "X-DSPAM-Confidence:    0.8475";

text = "X-DSPAM-Confidence:    0.8475";
spos = text.find(":")
trunctext = text[spos+1:40]
cleantext = trunctext.lstrip()
numtext = float(cleantext)
print numtext
