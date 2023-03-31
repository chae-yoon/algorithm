import sys
nums = []

for _ in range(5):
    nums.append(int(sys.stdin.readline().rstrip()))

nums.sort()

print(sum(nums) // 5)
print(nums[2])