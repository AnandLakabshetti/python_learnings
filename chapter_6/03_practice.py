
#identyfy the spam using text

text=input ("enter the text: ")

if ("make money" in text):
	spam=True
elif ("subscribe this" in text):
	spam=True
elif ("watch this" in text):
	spam=True
else :
	spam = False

if (spam):
	print ("this text is spam\n")
else:
	print ("this text is not spam\n")

