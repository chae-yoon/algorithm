import sys

N = int(sys.stdin.readline().rstrip())

for n in range(N-1, -1, -1):
    string = ' ' * (N-n-1) + '*' * (2*n + 1)
    print(string)