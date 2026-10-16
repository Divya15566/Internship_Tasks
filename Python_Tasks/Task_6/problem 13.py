# Problem 13: Set .union() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == '__main__':

    num_english_students = int(input())
    english_subs = set(map(int, input().split()))
    
    num_french_students = int(input())
    french_subs = set(map(int, input().split()))
    
    total_subs = english_subs.union(french_subs)

    print(len(total_subs))


