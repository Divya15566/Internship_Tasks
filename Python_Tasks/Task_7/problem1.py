# Problem 1: Set .symmetric_difference() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))

result = english_set.symmetric_difference(french_set)
print(len(result))
