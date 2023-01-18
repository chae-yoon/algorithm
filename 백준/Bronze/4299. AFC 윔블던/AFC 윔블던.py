import sys

add, minus = map(int, sys.stdin.readline().split())


A = (add + minus) // 2
B = add - A

if (add + minus) % 2 == 0 and A >= 0 and B >= 0:
    print(A, B) 

else:
    print(-1)