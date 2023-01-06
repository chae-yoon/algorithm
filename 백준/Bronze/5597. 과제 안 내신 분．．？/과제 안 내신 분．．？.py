import sys

student = list(range(1, 31))
check = []

for i in range(28):
   check.append(int(sys.stdin.readline().rstrip()))

result = list(set(student) - set(check))
result.sort()

for i in result:
    print(i)