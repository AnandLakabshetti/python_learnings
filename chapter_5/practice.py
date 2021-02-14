hindi={"aam":"mango","anar":"pomegranete","angur":"grapes"}

print (hindi.keys())
word=input ("enter the hindi word")
#below line will not give an error if key is not present 
print ("meaning of your word",hindi.get(word))
#below line will give an error if key is not present 
print ("meaning of your word",hindi[word])


