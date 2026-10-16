# Problem 20: Validating the Phone Number
# HackerRank Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com


import re

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        phone_number = input().strip()
        if re.match(r'^[789]\d{9}$', phone_number):
            print("YES")
        else:
            print("NO")
