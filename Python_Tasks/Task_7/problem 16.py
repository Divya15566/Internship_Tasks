# Problem 16: Caesar Cipher
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem


#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    k = k % 26
    result = []
    
    for char in s:
        if char.isupper():
            shifted_char = chr(ord('A') + (ord(char) - ord('A') + k) % 26)
            result.append(shifted_char)
        elif char.islower():
            shifted_char = chr(ord('a') + (ord(char) - ord('a') + k) % 26)
            result.append(shifted_char)
        else:
            result.append(char)
            
    return "".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
