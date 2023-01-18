import sys

L = int(sys.stdin.readline().rstrip())
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())

language = A // C if A % C == 0 else A // C + 1
math = B // D if B % D == 0 else B // D + 1

print(L - max(language, math))