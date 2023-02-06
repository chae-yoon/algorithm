import sys
sys.setrecursionlimit(10000)
def dfs(y, x):
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    
    graph[y][x] = 0

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == 1:
            dfs(ny,nx)

while True:
    W, H = map(int, sys.stdin.readline().split())
    land = 0

    if W == 0 and H == 0:
        break

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if graph[y][x] == 1:
                dfs(y,x)
                land += 1
                
    print(land)