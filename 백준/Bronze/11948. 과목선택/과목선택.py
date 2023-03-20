import sys

science = [int(sys.stdin.readline().rstrip()) for _ in range(4)]
science.sort(reverse=True)
science.pop()
social = [int(sys.stdin.readline().rstrip()) for _ in range(2)]
result = sum(science) + max(social)
print(result)