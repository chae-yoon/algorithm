import sys

T = int(sys.stdin.readline().rstrip())

for t in range(T):
    password = sys.stdin.readline().rstrip()

    if 6 <= len(password) <= 9:
        print('yes')
    else:
        print('no')