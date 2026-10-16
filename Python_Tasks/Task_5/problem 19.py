# Problem 19: Merge the Tools!
# HackerRank Link: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        chunk = string[i:i+k]
        unique_chunk = dict.fromkeys(chunk)
        print("".join(unique_chunk))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
