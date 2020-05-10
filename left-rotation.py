#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    p=[]
    r=[]
    p.append(a[:d])
    p.append(a[d:])
    p=p[1]+p[0]
    q = [str(i) for i in p]
    j = " ".join(q)
    print(j)

