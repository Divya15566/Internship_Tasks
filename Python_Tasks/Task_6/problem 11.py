# Problem 11: String Formatting
# HackerRank Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(format(n, "b"))
    for i in range(1, n+1):
        print(
            format(i, "d").rjust(width),
            format(i, "o").rjust(width),
            format(i, "X").rjust(width),
            format(i, "b").rjust(width)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
