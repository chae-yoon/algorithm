import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
result = 0

for _ in range(N):
    S.add(sys.stdin.readline().rstrip())

for _ in range(M):
    word = sys.stdin.readline().rstrip()
    if word in S:
        result += 1

print(result)