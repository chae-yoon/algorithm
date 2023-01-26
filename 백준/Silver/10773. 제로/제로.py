import sys

K = int(sys.stdin.readline().rstrip())
stack = []

for k in range(K):
    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        stack.pop()
    
    else:
        stack.append(num)

print(sum(stack))