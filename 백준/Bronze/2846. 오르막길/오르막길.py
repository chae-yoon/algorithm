import sys

N = int(sys.stdin.readline().rstrip())

roads = list(map(int, sys.stdin.readline().split()))
heights = []
height = 0

for index in range(N-1):
    if roads[index+1] - roads[index] > 0:
        height += roads[index+1] - roads[index]
    else:
        if height >= 2:
            heights.append(height)
            height = 0
        else:
            height= 0

heights.append(height)

print(sorted(heights).pop() if len(heights) > 0 else 0)