# Create a file
myfile = open("testfile.txt","w+")
# 'w' Write the file
# '+' create if does not exist

# Append to file
for i in range(10):
     myfile.write("This is line %d\r\n" % (i+1))


