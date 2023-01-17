import sys

N, M = map(int, sys.stdin.readline().split())

print(N - M if N - M > 0 else M - N)