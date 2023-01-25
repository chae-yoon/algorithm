import sys

while True:
    sides = list(map(int, sys.stdin.readline().split()))

    if sides.count(0) == 3:
        break

    sides.sort()

    print('right' if sides[0]**2 + sides[1]**2 == sides[2]**2 else 'wrong')