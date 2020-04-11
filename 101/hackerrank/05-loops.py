#Read an integer N . For all non-negative integers  i<N, print i2 . See the sample for details.

if __name__ == '__main__':
    n = int(input())

# For loop
for i in range(0, n):
    if i > 20:
        break


    print(i**2)


# While
#i = 0
#while i < 5:
    #print i
    #i += 1