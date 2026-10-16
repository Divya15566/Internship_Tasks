# Problem 16: Nested Lists
# HackerRank Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    scores = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score) 
        
    second_lowest_score = sorted(scores)[1]
    
    runner_ups = [name for name, score in students if score == second_lowest_score]
    
    for name in sorted(runner_ups):
        print(name)
