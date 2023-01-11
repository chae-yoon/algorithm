A, B = map(int, input().split())

if A > B:
    if A - B == 2:
        print('B')
    else:
        print('A')
else:
    if A - B == -2:
        print('A')
    else:
        print('B')