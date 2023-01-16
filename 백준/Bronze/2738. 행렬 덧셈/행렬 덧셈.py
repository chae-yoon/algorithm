import sys

N, M = map(int,sys.stdin.readline().split())
arrays = []

for i in range(2):  
    for n in range(N):
        lis= list(map(int, sys.stdin.readline().split()))
        arrays.append(lis)

for n in range(N):
    result = [x + y for x, y in zip(arrays[n], arrays[n+N])]
    print(*result)