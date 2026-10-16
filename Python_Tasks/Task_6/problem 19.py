# Problem 19: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    sorted_string = sorted(s.strip())
    char_counts = Counter(sorted_string)
    top_three = char_counts.most_common(3)
    for char, count in top_three:
        print(f"{char} {count}")
