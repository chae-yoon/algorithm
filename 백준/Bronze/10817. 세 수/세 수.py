import sys, heapq

nums = list(map(int, sys.stdin.readline().split()))
heapq.heapify(nums)
heapq.heappop(nums)
print(heapq.heappop(nums))