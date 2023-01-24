import sys

M = sys.stdin.readline().rstrip()
result = 1
exist = False

def constructor(N: str):
    result = int(N)
    for n in N:
        result += int(n)
    
    return result

while result < int(M):
    if constructor(str(result)) == int(M):
        exist = True
        break

    result += 1

print(result if exist else 0)