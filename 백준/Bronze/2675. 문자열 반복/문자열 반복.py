import sys

N = int(input())

for i in range(N):
    R, S = sys.stdin.readline().split()
    P = ''

    for char in S:
        P += char * int(R)

    print(P)