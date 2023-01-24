import sys

T = int(sys.stdin.readline().rstrip())

for t in range(T):
    string = sys.stdin.readline().rstrip()
    check = 0
    
    for s in string:
        if string[0] == '(' and string[-1] == ')':
            if s == '(':
                check += 1
            else:
                if check > 0:
                    check -= 1
                else:
                    check = -1
                    break
        else:
            check = -1

    if check == 0:
        print('YES')
    else:
        print('NO')