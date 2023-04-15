import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    nums = list(map(int, sys.stdin.readline().split()))
    print(sum(nums))