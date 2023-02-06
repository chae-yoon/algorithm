import sys
totals, total = [], 0

for _ in range(4):
    get_off, get_on = map(int, sys.stdin.readline().split())
    total += get_on - get_off
    totals.append(total)

print(max(totals))