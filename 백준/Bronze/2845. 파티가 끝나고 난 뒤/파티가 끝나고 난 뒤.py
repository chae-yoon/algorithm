import sys

L, P = map(int, sys.stdin.readline().split())
news = list(map(int, sys.stdin.readline().split()))

results = [l - L * P for l in news]

print(*results)