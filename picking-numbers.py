#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    l=[]
    p=[]
    arr=sorted(a)
    #max_v=0
    for i in arr:
        if i not in l:
            l.append(i)
    print(l)
    if(len(l)>1):
        for i in range(1,len(l)):
        #print(abs((l[i-1]-l[i])))

            if  (l[i]-l[i-1])<=1 :
                print(l[i]-l[i-1])
                p.append(arr.count(l[i-1])+arr.count(l[i]))
                print(arr.count(l[i-1]))
                print(arr.count(l[i]))
                print(p)
                print('#####')

    else:
        p=[len(arr)]
    return max(p)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
