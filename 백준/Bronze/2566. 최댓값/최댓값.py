import sys

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
max_num = max(map(max, matrix))

for y in range(9):
    for x in range(9):
        if matrix[y][x] == max_num:
            row, column = y, x
            break

print(max_num)
print(row+1, column+1)