#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p=0;n=0;z=0
    p=list(filter(lambda x :(x>0),arr))
    print(len(p)/len(arr))
    n=list(filter(lambda x :(x<0),arr))
    print(len(n)/len(arr))
    z=list(filter(lambda x :(x==0),arr))
    print(len(z)/len(arr))
    
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
