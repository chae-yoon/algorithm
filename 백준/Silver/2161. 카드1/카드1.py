import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
queue = deque(range(1, N+1))

for n in range(N):
    print(queue.popleft(), end=' ')
    try:
        num = queue.popleft()
        queue.append(num)
    except:
        break