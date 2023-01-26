import sys

T = int(sys.stdin.readline().rstrip())

for t in range(T):
    changes = {
        25: 0,
        10: 0,
        5: 0,
        1: 0,
    }

    money = int(sys.stdin.readline().rstrip())

    for change in changes:
        changes[change] = money // change
        money %= change

    print(*changes.values())