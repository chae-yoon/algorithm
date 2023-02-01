import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    scores = list(map(int, sys.stdin.readline().split()))
    scores.sort()
    print(sum(scores[1:4]) if scores[3] - scores[1] < 4 else 'KIN')