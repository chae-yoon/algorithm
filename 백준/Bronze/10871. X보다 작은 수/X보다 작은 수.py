import sys

n, v = map(int, sys.stdin.readline().split(' '))
lis = map(int, sys.stdin.readline().split(' '))
result = []

for num in lis:
    if num < v:
        result.append(str(num))

print(' '.join(result))