import sys, math

N, K = map(int, sys.stdin.readline().split())

print(math.factorial(N)//(math.factorial(K)*math.factorial(N-K)))