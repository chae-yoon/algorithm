import sys, math

A, B, C = map(int, sys.stdin.readline().split())

result1 = math.trunc(A / B * C)
result2 = math.trunc(A * B / C)

print(max(result1,result2))