##question 1 --> string1 +string2
str=input ("enter the your name \n")
print ("good morning "+str)\

##question 2 -->letter template using '''

str='''hi sir
branch manager
BOM pune

	hi sir,
	as subject mentioned i want to thank you for providing me support.

Thanks
Anand Lakabshetti '''


print (str)


##delete double spaces from the line

str="my  name is    anand  "
print (str.replace("  "," "))
str="my  \nname \tis  \t  anand  "
print (str.replace("  "," "))
