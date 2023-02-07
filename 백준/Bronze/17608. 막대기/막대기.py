import sys

stack = []
for _ in range(int(sys.stdin.readline().rstrip())):
    stack.append(int(sys.stdin.readline().rstrip()))

max_height = stack.pop()
height = 1

while stack:
    now = stack.pop()

    if now > max_height:
        max_height = now
        height += 1
    
print(height)