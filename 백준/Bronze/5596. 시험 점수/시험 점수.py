import sys

S = list(map(int, sys.stdin.readline().split()))
T = list(map(int, sys.stdin.readline().split()))

print(sum(S) if sum(S) >= sum(T) else sum(T))