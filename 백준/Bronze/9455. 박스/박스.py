import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    M, N = map(int, sys.stdin.readline().split())
    boxes = [[] for _ in range(M)]
    rotate_boxes = [[0]*M for _ in range(N)]
    shift = 0

    for m in range(M):
        boxes[m] = list(map(int, sys.stdin.readline().split()))

    for n in range(N):
        for m in range(M):
            rotate_boxes[n][m] = boxes[-m-1][n]

    for box in rotate_boxes:
        empty = 0
        for b in box:
            if b == 1:
                shift += empty
                continue
            
            empty += 1

    print(shift)