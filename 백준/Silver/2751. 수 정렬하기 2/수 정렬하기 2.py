import sys

N = int(sys.stdin.readline().rstrip())

numbers = [int(sys.stdin.readline().rstrip()) for n in range(N)]

print(*sorted(numbers), sep='\n')