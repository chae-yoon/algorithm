import sys, heapq

nums = []
heapq.heapify(nums)

for _ in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        print(-heapq.heappop(nums) if len(nums) > 0 else 0)
    
    else:
        heapq.heappush(nums, -num)