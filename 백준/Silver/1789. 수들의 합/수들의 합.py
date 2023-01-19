import sys

num = int(sys.stdin.readline().rstrip())
start, result = 1, 0

while result <= num:
    result += start
    start += 1

print(start-2)