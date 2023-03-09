T = int(input())
results = []

for t in range(1, T + 1):
    if T % t == 0:
        results.append(t)

print(*results)