# Problem 10: Swap Case
# HackerRank Link: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result = ""
    for i in s:
        if i.isupper():
            result+=i.lower()
        elif i.islower():
            result+=i.upper()
        else:
            result+=i
   
    return result 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
