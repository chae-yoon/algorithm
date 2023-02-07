import sys

N = int(sys.stdin.readline().rstrip())
big_dict = {}
biggers = [0]*N

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    big_dict[_] = (x, y)

for index, info in big_dict.items():
    rank = 0

    for x, y in big_dict.values():
        if info[0] < x and info[1] < y:
            rank += 1
    
    biggers[index] = rank+1

print(*biggers)