# Problem 10: Designer Door Mat
# HackerRank Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

N, M = map(int, input().split())
c = ".|."
mid = N // 2
for i in range(0, mid):
    print((c*(2*i+1)).center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(mid-1,-1,-1):
    print((c*(2*i+1)).center(M,"-"))
