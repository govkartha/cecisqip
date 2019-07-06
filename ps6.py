import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    p=[0,0]
    if a[0] > b[0]:
        p[0] +=1
    elif a[0] < b[0]:
        p[1] +=1
    if a[1] > b[1]:
        p[0] += 1
    elif a[1] < b[1]:
        p[1] += 1
    if a[2] > b[2]:
        p[0] += 1
    elif a[2] < b[2]:
        p[1] +=1
    if a[0] == b[0] or a[1] == b[1] or a[2] == b[2]:
        p[0]+=0
        p[1]+=0
    return p

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
