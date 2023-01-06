import sys

lis = []

for i in range(9):
    lis.append(int(sys.stdin.readline().rstrip()))

print(max(lis))
print(lis.index(max(lis))+1)