import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)