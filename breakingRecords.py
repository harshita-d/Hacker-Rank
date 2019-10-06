#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min=scores[0]
    max=scores[0]
    c=0
    f=0
    for i in range(len(scores)):
        if max<scores[i]:
            max=scores[i]
            c=c+1
        elif min>scores[i]:
            min=scores[i]
            f=f+1
    return c,f

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
