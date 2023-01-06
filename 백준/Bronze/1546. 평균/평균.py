import sys

N = int(sys.stdin.readline().rstrip())
scores = list(map(int, sys.stdin.readline().split(' ')))
new_scores = []

max_score = max(scores)

for score in scores:
    new_scores.append(score / max_score * 100)
    
print(sum(new_scores)/N)