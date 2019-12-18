# https://www.learnpython.org/
# https://realpython.com/
# https://realpython.com/learning-paths/python-devops/

# Hello, World!
print("Hello Xavier") #Hello Xavier

# Indentation
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

    # x is 1.


# Numbers
myint = 7
print(myint)
# float
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# Strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)

# Additions
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Multi assignements
a, b = 3, 4
print(a,b)


# lists
x = object()
y = object()

## TODO: change this code
x_list = [x,x,x,x,x,x,x,x,x,x]
y_list = [y,y,y,y,y,y,y,y,y,y]
big_list = x_list+ y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

## testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


# FORMAT

'{0} and {1} and {2}'.format("premier", "deuxieme", "troisieme")
#'premier and deuxieme and troisieme'