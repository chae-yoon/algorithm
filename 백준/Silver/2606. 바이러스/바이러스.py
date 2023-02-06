import sys

computers = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(computers+1)]
visited = [False]*(computers+1)

def dfs(index):
    stack = [index]
    visited[index] = True

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
                
for _ in range(int(sys.stdin.readline().rstrip())):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)
print(visited.count(True)-1)