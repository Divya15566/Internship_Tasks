# Problem 17: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def separateNumbers(s):
    if len(s) <= 1:
        print("NO")
        return
    for i in range(1, (len(s) // 2) + 1):
        first_num_str = s[:i]
        if first_num_str[0] == '0' and len(first_num_str) > 1:
            continue
        prev = int(first_num_str)
        generated_str = first_num_str
        while len(generated_str) < len(s):
            next_num = prev + 1
            generated_str += str(next_num)
            prev = next_num
        if generated_str == s:
            print(f"YES {first_num_str}")
            return       
    print("NO")
    
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
