# !/bin/python3

import math
import os
import random
import re
import sys


def alternatingCharacters(s):
    # Write your code here
    cont = 0
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cont += 1
    return cont
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()