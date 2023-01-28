import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
nums = deque()

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        nums.append(command[1])
    elif command[0] == 'pop':
        print(nums.popleft() if len(nums) > 0 else -1)
    elif command[0] == 'size':
        print(len(nums))
    elif command[0] == 'empty':
        print(1 if len(nums) == 0 else 0)
    elif command[0] == 'front':
        print(nums[0] if len(nums) > 0 else -1)
    elif command[0] == 'back':
        print(nums[-1] if len(nums) > 0 else -1)