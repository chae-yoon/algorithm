import sys

N, M = sys.stdin.readline().split()
M_sum = sum(map(int, M))
result = 0

for n in N:
    result += int(n) * M_sum

print(result)