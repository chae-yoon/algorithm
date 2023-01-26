import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
queue = deque()

for n in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        queue.appendleft(int(command[-1]))
    elif command[0] == 'push_back':
        queue.append(int(command[-1]))
    elif command[0] == 'pop_front':
        print(queue.popleft() if len(queue) > 0 else -1)
    elif command[0] == 'pop_back':
        print(queue.pop() if len(queue) > 0 else -1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(int(len(queue) == 0))
    elif command[0] == 'front':
        print(queue[0] if len(queue) > 0 else -1)
    elif command[0] == 'back':
        print(queue[-1] if len(queue) > 0 else -1)