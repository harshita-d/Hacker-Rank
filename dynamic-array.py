#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    lastanswer=0
    p=0
    q=[]
    seq=[]
    for i in range(n):
        seq.append([])
    for i in range(len(queries)):
        z,x,y=queries[i][0],queries[i][1],queries[i][2]
        p=((x^lastanswer)%n)
        if z==1:
            seq[p].append(y)
        else:
            lastanswer=seq[p][(y%(len(seq[p])))]
            q.append(lastanswer)
    return q


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

