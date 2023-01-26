import sys, math

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
result = []

for number in numbers:
    result.append(number)
    if number == 1:
        result.pop()
        
    for n in range(2, number):
        if math.gcd(n, number) > 1:
            result.pop()
            break

print(len(result))