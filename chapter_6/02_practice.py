
sub1=int (input ("enter the first subject1 marks\n"))
sub2=int (input ("enter the first subject2 marks\n"))
sub3=int (input ("enter the first subject3 marks\n"))

if (sub1 <33 or sub2 <33 or sub3 <33):
	print ("you are failed \n")
elif ((sub1+sub2+sub3)/3 < 40):
	print ("you are failed due to aggreagare marks are not 40%")
else:
	print ("congradulation you are passed now \n")
