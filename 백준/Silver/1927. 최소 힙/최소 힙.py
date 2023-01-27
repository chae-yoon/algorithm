import sys, heapq

N = int(sys.stdin.readline().rstrip())
numbers = []
heapq.heapify(numbers)

for n in range(N):
    x = int(sys.stdin.readline().rstrip())
    
    if len(numbers) == 0 and x == 0:
        print(0)
    
    elif x == 0:
        print(heapq.heappop(numbers))
    
    else:
        heapq.heappush(numbers, x)