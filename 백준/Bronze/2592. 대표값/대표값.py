from collections import Counter
import sys

nums= [0] * 10

for _ in range(10):
    nums[_] = int(sys.stdin.readline().rstrip())
print(sum(nums)//10)

nums_count = Counter(nums).most_common()
print(nums_count[0][0])