# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'funnyString' function below.

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def funnyString(s):
    # Write your code here
    normal=[ ord(c) for c in s]
    rev = [ord(c) for c in s[::-1]]
    for i in range(1,len(s)):
      resta = abs(normal[i]-normal[i-1])
      resta_reves = abs(rev[i]-rev[i-1])
      if resta != resta_reves:
        return 'Not Funny'
    return 'Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()