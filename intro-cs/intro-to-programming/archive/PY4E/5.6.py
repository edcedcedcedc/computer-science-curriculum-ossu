text = "X-DSPAM-Confidence:    0.8475"
colonindex = text.find(":")
substring = text[colonindex+1:].lstrip()
print(float(substring))
