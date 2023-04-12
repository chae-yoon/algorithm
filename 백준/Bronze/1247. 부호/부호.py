import sys

for _ in range(3):
    cycle = int(sys.stdin.readline().rstrip())
    nums = []
    for _ in range(cycle):
        nums.append(int(sys.stdin.readline().rstrip()))

    if sum(nums) == 0:
        print(0)
    elif sum(nums) > 0:
        print('+')
    else:
        print('-')