
#set is collecton of non repetative elements
#a=set()->empty set, and a={}->it is empty dictionary
a={1,2,3,5}
print (a)
print (type(a))

print (a.remove(3))
print (a)
#we cannot add the LIST,DICTIONARY as set is not hashable in set but we can add tuple(immutable)

#properties
##unordered , unindexed,
#there is no way to change the items in sets
#adding a same value repeatatively does not change the set
#dont remove the number/element which is not available, it will throw the error

#methods of the set
#length of the set
print (len (a))
#pop the any  element from the set
print (a.pop())
#
print (a.clear())
print (len (a))
a.add((1,2,3))
print ((a))
#union including both generate the unique i.e non repeatative elements set
print (a.union({2,3}))
#intersection i.e elements which are available in both the sets 
print (a.intersection({2,3}))



