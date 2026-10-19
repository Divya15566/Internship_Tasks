# Problem 7: Alphabet Rangoli
# HackerRank Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    width = 4 * size - 3  
    rows = []
    
    for i in range(size):
        L = [alpha[size-1-j] for j in range(i+1)]
        R = L[:-1][::-1]               
        row = "-".join(L + R)          
        rows.append(row.center(width, "-"))
    for r in rows + rows[-2::-1]:
        print(r)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
