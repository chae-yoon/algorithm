def solution(board):
    answer = 0
    new_board = [['O']*len(board) for _ in range(len(board))]

    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 1:
                new_board[y][x] = 'X'

                for index in range(8):
                    nx, ny = x+dx[index], y+dy[index]
                    if 0<=nx<len(board) and 0<=ny<len(board):
                        new_board[ny][nx] = 'X'

    for x in new_board:
        answer += x.count('X')

    answer = len(board)*len(board) - answer
    return answer