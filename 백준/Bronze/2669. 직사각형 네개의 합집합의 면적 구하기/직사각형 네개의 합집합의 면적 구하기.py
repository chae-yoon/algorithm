import sys

set_r = set()

for _ in range(4):
    r_place = list(map(int, sys.stdin.readline().split()))

    for n in range(r_place[0], r_place[2]):
        for m in range(r_place[1], r_place[3]):
            set_r.add((n,m))

print(len(set_r))