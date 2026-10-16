# Problem 12: Capitalize!
# HackerRank Link: https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    result = ""
    for i in range(len(s)):
        if i == 0 and s[i].isalpha():
            result += s[i].capitalize()
        elif s[i-1] == " " and s[i].isalpha():
            result+=s[i].capitalize()
        else:
            result+=s[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
