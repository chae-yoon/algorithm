N = int(input())
multy_two = []

for i in range(N+1):
    multy_two.append(2 ** i)

print(*multy_two)