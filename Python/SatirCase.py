#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    artericos = '#'
    for  i in range(n):
        pos=i+1
        asteriscos = artericos * pos
        print(asteriscos.rjust(n))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)