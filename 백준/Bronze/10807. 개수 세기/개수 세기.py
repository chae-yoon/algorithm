import sys

N = int(sys.stdin.readline().rstrip())
list_num = map(int, sys.stdin.readline().split(' '))
v = int(sys.stdin.readline().rstrip())
count = 0

for num in list_num:
    if num == v:
        count += 1

print(count)