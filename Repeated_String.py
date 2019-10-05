#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count=s.count("a")
    q=n//len(s)
    r=n%len(s)
    q=q*count
    for i in range(r):
        if s[i]=="a":
            q=q+1
    return q

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
