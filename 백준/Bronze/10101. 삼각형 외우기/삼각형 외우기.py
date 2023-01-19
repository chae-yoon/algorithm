import sys

angle = [int(sys.stdin.readline().rstrip()) for n in range(3)]

if sum(angle) != 180:
    print('Error')

else:
    set_angle = set(angle)

    if len(set_angle) == 1:
        print('Equilateral')
    
    elif len(set_angle) == 2:
        print('Isosceles')
    
    else:
        print('Scalene')