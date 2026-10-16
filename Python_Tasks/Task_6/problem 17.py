# Problem 17: Check Strict Superset
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

if __name__ == '__main__':
    set_A = set(map(int, input().split()))
    num_other_sets = int(input())
    is_strict_superset = True
    
    for _ in range(num_other_sets):
        other_set = set(map(int, input().split()))
        if not (set_A > other_set):
            is_strict_superset = False
            break 
            
    print(is_strict_superset)
