N = int(input())
numbers = []

for n in range(N):
    numbers.append(int(input()))

numbers.sort()
print(*numbers, sep='\n')