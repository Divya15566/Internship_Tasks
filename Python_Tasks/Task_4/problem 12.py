# problem 12: Introduction to Sets
# HackerRank Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    distinct_elements = set(array)
    avg = sum(distinct_elements) / len(distinct_elements)
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
