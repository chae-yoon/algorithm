import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
queue = deque(range(1, N+1))
new_queue = []

for n in range(N):
    queue.rotate(-K+1)
    new_queue.append(queue.popleft())

print('<', end='')
print(*new_queue, sep=', ', end='')
print('>')