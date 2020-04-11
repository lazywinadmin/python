2#!/bin/python3

import math
import os
import random
import re
import sys


# Main script
if __name__ == '__main__':
    #print("Enter an Integer: ")
    n = int(input().strip())

# odd or even ?
ntype = n % 2

if ntype != 0: # Weird
    print("Weird")
elif ntype == 0 and (2 <= n <= 5):
    print("Not Weird")
elif ntype == 0 and (6 <= n <= 20):
    print("Weird")
elif ntype == 0 and (n > 20):
    print("Not Weird")