import sys
scores = [()]*5

for n in range(5):
    score = list(map(int, sys.stdin.readline().split()))
    scores[n] = (n+1, sum(score))

score_sort = sorted(scores, key=lambda x:x[1])

print(*score_sort.pop())