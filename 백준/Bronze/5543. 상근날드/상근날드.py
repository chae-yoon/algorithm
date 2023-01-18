import sys

top = int(sys.stdin.readline().rstrip())
middle = int(sys.stdin.readline().rstrip())
bottom = int(sys.stdin.readline().rstrip())
cola = int(sys.stdin.readline().rstrip())
cider = int(sys.stdin.readline().rstrip())

print(min(top,middle,bottom) + min(cola, cider) - 50)