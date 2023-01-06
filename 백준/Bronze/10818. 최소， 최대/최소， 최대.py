import sys

n = int(sys.stdin.readline().rstrip())
lis = map(int, sys.stdin.readline().split(' '))

list_num = list(lis)

print(min(list_num), max(list_num))