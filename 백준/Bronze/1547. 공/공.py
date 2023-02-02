import sys

ball = 1

for _ in range(int(sys.stdin.readline().rstrip())):
    X, Y = map(int, sys.stdin.readline().split())
    
    if ball == X:
        ball = Y

    elif ball == Y:
        ball = X

print(ball)