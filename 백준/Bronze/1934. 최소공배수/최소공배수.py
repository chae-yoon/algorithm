import sys, math

for _ in range(int(sys.stdin.readline().rstrip())):
    A, B = map(int, sys.stdin.readline().split())
    result = math.lcm(A, B)

    print(result)