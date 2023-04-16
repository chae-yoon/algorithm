import sys

while True:
    num = sys.stdin.readline().rstrip()

    if num == '0':
        break

    row = len(num) + 1
    for n in num:
        if n == '0':
            row += 4
        elif n == '1':
            row += 2;
        else:
            row += 3
    print(row)