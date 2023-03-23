import sys

M = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())

if M < 2:
    print('Before')
elif M == 2:
    if D < 18:
        print('Before')
    elif D == 18:
        print('Special')
    else:
        print('After')
else:
    print('After')