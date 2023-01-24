import sys

T = int(sys.stdin.readline().rstrip())

for t in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    floor = N % H if N % H != 0 else H
    houses = N // H if floor == H else N // H + 1
    print(f'{floor}{houses if houses > 10 else str(houses).rjust(2, str(0))}')