mylist = [0,1,2,3,"Bob"]

print(mylist)
print(mylist[1])
print(mylist[1:]) # grab from one
print(mylist[1:4]) # grab from one

# replace a value
mylist[1] = "Mike"
print(mylist[1])

# list functions
mylist.append("Xavier")
print(mylist)

anotherlist = [ "yellow", "red"]
mylist.extend(anotherlist)
print(mylist)

mylist.insert(1,"Cow") # add item at index specified
print(mylist)

mylist.remove("Mike")
print(mylist)

#mylist.clear()
#print(mylist)

mylist.pop() # remove the last item
print(mylist)

print(mylist.index("Xavier")) # return the index of Xavier
#print(mylist.index("Jeff")) # error out if not exist in list

print(mylist.count("Xavier"))


# mylist.sort() # only work on numbers
# mylist.reverse() # only work on numbers

# Create a copy
mylist2 = mylist.copy()

print(mylist2)

