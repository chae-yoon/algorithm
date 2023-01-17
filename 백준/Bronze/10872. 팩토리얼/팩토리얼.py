import sys

N = int(sys.stdin.readline().rstrip())
pack = 1

for n in range(1, N + 1):
    pack *= n

print(pack)