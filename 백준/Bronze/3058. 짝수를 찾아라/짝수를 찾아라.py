import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    numbers = list(map(int, sys.stdin.readline().split()))
    evens = [num for num in numbers if num % 2 == 0]
    print(sum(evens), min(evens))