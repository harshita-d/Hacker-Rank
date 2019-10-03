#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    c=":"
    s1=s.split(":")
    s2=s.find("PM")
    if s2>-1:
        if s1[0]!="12":
            s1[0]=int(s1[0])+12
            s1[0]=str(s1[0])
            s1=c.join(s1)
            s1=s1.rstrip("PM")
        else:
            s1=c.join(s1)
            s1=s1.rstrip("PM")
    else:
        if s1[0]!="12":
            s1=c.join(s1)
            s1=s1.rstrip("AM")
        else:
            s1[0]="00"
            s1=c.join(s1)
            s1=s1.rstrip("AM")
    return s1
     
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
