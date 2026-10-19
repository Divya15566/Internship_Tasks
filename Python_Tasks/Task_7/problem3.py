# Problem 3: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def marsExploration(s):
    pattern = "SOS"
    altered_count = 0
    
    for i in range(len(s)):
        if s[i] != pattern[i % 3]:
            altered_count += 1
            
    return altered_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
