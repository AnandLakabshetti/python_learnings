
friends=["anand","amit","vishal","bharat","Amul"]
friend=["anand","amit","vishal",11,23.5]

print (friends[:])
print (friend[:])
print (friends[2:])
print (friends[:2])
friends.reverse()

print ("after reverse",friends[:])
friends.sort()
print ("after sort",friends[:])
friends.append(22)
print ("after append(22)",friends[:])
friends.insert(3,"naveen")
print ("after insert (3,'naveen')",friends[:])
friends.remove("anand")
print ("after remove ('anand')",friends[:])
