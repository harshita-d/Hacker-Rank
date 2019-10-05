#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    p=0
    q=0
    for i in range(n):
        if s[i]=="U":
            p=p+1
            if p==0:
                q=q+1
        else:
            p=p-1
    return q

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
