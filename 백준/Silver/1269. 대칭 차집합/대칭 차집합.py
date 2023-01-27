import sys

N, M = map(int, sys.stdin.readline().split())
An = list(map(int,sys.stdin.readline().split()))
Bn = list(map(int,sys.stdin.readline().split()))
A = set(An)
B = set(Bn)

print(len(A-B)+len(B-A))