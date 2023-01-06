import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    string = '*' * (i+1)
    print(string.rjust(N, ' '))