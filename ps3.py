#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    
    a=[]
    s=0
    for i in ar :
        if i not in a:
            a.append(i)
    for i in a :
        c=0
        for j in ar:
            if j==i:
                c+=1
        s+=int(c/2)
    return s

            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
