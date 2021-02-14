mydict={"name":"Anand","surname":"Lakabshett","marks":23, "another":{"name":"anand","surname":"lakabshetti"}}

print (mydict.keys())
print (mydict.values())
print (mydict['another']['name'])

print (mydict.items())#->it gives in key value pair all content of dictionary
mydict.update({"Name":"AnanD"})

#diff between .get and dict["kay"]
#mydict[] ->will give error if key is not present then but .get returns none

print (mydict.get("nAme"))
print (mydict["nAme"])

print (mydict.keys())
print (mydict.items())#->it gives in key value pair all content of dictionary
