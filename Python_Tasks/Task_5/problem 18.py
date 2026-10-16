# Problem 18: The Minion Game
# HackerRank Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    vowels = set("AEIOU")

    for i in range(length):
        substring_count = length - i
        if string[i] in vowels:
            kevin_score += substring_count
        else:
            stuart_score += substring_count

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
