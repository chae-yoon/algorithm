import sys

K, N, M = map(int, sys.stdin.readline().split())

if K * N > M:
    money = K * N - M
    print(money)
else:
    print(0)