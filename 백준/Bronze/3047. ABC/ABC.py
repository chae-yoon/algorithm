import sys

nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
num_dict = {
    'A': nums[0],
    'B': nums[1],
    'C': nums[2],
}

string = sys.stdin.readline().rstrip()
for s in string:
    print(num_dict[s], end=' ')