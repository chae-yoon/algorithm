import sys

string = sys.stdin.readline().rstrip()
vowels = ['a', 'e', 'i', 'o', 'u']
result = 0

for v in vowels:
    result += string.count(v)

print(result)