# Problem 20: Piling Up!
# HackerRank Link: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def can_stack_cubes(cubes_deque):
    current_top = float('inf')
    while cubes_deque:
        if cubes_deque[0] >= cubes_deque[-1]:
            chosen_cube = cubes_deque.popleft()
        else:
            chosen_cube = cubes_deque.pop()
        if chosen_cube > current_top:
            return "No"
        current_top = chosen_cube     
    return "Yes"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cubes = deque(map(int, input().split()))
        print(can_stack_cubes(cubes))
