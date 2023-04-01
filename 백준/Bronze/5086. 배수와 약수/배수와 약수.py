import sys

while True:
    num1, num2 = map(int, sys.stdin.readline().split())

    if num1 == 0 and num2 == 0:
        break

    if num1 % num2 == 0:
        print('multiple')
    elif num2 % num1 == 0:
        print('factor')
    else:
        print('neither')