#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    c=1
    t=0
    if p==1:
        return 0
    for i in range(2,n+1,2):
        if i==p or i+1==p:
            break
        c=c+1
    for i in range(2,n+1,2):
        t=t+1
    
    print(c,abs(t-c))
    return min(c,abs(t-c))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
