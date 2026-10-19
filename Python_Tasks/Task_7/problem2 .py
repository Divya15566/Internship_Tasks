# Problem 2: The Captain's Room
# HackerRank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    k = int(input())
    room_list = list(map(int, input().split()))
    room_set = set(room_list)
    captains_room = (sum(room_set) * k - sum(room_list)) // (k - 1)
    print(captains_room)
