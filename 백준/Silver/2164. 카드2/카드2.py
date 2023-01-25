import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

queue = deque(range(1, N+1))

while len(queue) > 1:
    queue.popleft()
    q = queue.popleft()
    queue.append(q)
    
print(*queue)