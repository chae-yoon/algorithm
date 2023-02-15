import sys

X, Y = sys.stdin.readline().split()

rev_x = int(X[::-1])
rev_y = int(Y[::-1])
rev_x_y = int(str(rev_x + rev_y)[::-1])

print(rev_x_y)