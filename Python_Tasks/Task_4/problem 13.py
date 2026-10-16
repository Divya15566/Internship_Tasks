# problem 13: Symmetric Difference
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':

    m_size = int(input())
    m_set = set(map(int, input().split()))
    
    n_size = int(input())
    n_set = set(map(int, input().split()))
    
    sym_diff = m_set ^ n_set
    for element in sorted(sym_diff):
        print(element)
