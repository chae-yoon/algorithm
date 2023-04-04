import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())
    result = 'even' if num % 2 == 0 else 'odd'
    print(result)