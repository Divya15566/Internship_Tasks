# Problem 16: Check Subset
# HackerRank Link: http://hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    test_cases = int(input())
    
    for i in range(test_cases):
        size_A = int(input())
        set_A = set(map(int, input().split()))
        
        size_B = int(input())
        set_B = set(map(int, input().split()))
        
        print(set_A.issubset(set_B))
