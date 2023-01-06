import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    score = sys.stdin.readline().rstrip()
    O = 0
    result = 0

    for char in score:
        if char == 'O':
            O += 1
            result += O
        else:
            O = 0
    
    print(result)