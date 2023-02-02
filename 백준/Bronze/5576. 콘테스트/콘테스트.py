import sys, heapq

scores_W, scores_K = [], []
sum_W, sum_K = 0, 0

heapq.heapify(scores_W)
heapq.heapify(scores_K)

for _ in range(10):
    heapq.heappush(scores_W, -int(sys.stdin.readline().rstrip()))

for _ in range(10):
    heapq.heappush(scores_K, -int(sys.stdin.readline().rstrip()))

for _ in range(3):
    sum_W += -heapq.heappop(scores_W)
    sum_K += -heapq.heappop(scores_K)

print(sum_W, sum_K)