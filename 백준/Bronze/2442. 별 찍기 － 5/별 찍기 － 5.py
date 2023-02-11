import sys

N = int(sys.stdin.readline().rstrip())

for n in range(0, N):
    string = ' ' * (N-n-1) + '*' * (2*n + 1)
    print(string)