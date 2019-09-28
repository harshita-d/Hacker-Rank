#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    lst=[]
    p=0
    x=0
    sum1=0
    while(p<5):
        for i in range(5):
            if(x==i):
                continue
            else:
                sum1=sum1+arr[i]
        x=x+1
        lst.append(sum1)
        sum1=0
        p=p+1
    print(min(lst),max(lst))



        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
