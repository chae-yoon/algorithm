import sys

N = int(sys.stdin.readline().rstrip())

for n in range(N, 0, -1):
    print('*' * n)