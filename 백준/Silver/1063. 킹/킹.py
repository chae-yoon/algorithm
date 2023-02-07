import sys

directions = {
    'R' : (0,1),
    'L' : (0, -1),
    'B' : (1,0),
    'T' : (-1,0),
    'RT' : (-1,1),
    'LT' : (-1,-1),
    'RB' : (1,1),
    'LB' : (1,-1),
}

board = [['0']*8 for _ in range(8)]

K, R, N = sys.stdin.readline().split()

kx, ky = ord(K[0])-65, 8-int(K[1])
rx, ry = ord(R[0])-65, 8-int(R[1])

for _ in range(int(N)):
    dy, dx = directions[sys.stdin.readline().rstrip()]
    knx, kny = kx+dx, ky+dy

    if knx == rx and kny == ry:
        rnx, rny = rx+dx, ry+dy
        if not (0 <= rnx < 8 and 0 <= rny < 8):
            continue
    else:
        rnx, rny = rx, ry

    if 0 <= knx < 8 and 0 <= kny < 8:
        kx, ky = knx, kny
    if 0 <= rnx < 8 and 0 <= rny < 8:
        rx, ry = rnx, rny

print(chr(kx+65)+str(8-ky))
print(chr(rx+65)+str(8-ry))