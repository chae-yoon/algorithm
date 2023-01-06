import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    lis = list(map(int, sys.stdin.readline().split(' ')))

    avg = sum(lis[1:]) / (len(lis)-1)
    count = 0

    for j in lis[1:]:
        if j > avg:
            count += 1
    
    percent = count/lis[0]

    print(f'{percent:.3%}')