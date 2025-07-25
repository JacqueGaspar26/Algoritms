#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
  # Write your code here
  n= len(arr)
  positivo = 0
  negativo = 0
  cero = 0
  for i in arr:
    if i>0:
      positivo += 1
    elif i<0:
      negativo += 1
    else:
      cero += 1
  print(round(positivo / n, 6))
  print(round(negativo / n, 6))
  print(round(cero / n, 6))
if __name__ == '__main__':
  n = int(input().strip())
  arr = list(map(int, input().rstrip().split()))
  plusMinus(arr)

