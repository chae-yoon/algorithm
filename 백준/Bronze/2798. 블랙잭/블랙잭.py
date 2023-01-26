import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
max_sum = 0

cards.sort()

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            now = cards[i]+cards[j]+cards[k]
            if now <= M and now > max_sum:
                x, y, z = i, j, k
                max_sum = now

print(max_sum)