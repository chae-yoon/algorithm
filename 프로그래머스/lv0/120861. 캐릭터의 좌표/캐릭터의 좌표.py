def solution(keyinput, board):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    width = board[0] // 2
    height = board[1] //2
    guide = [0,0]
    
    for kinput in keyinput:
        if kinput == 'up':
            if -width <= guide[0] + dx[0] <= width and -height <= guide[1] + dy[0] <= height:
                guide[0] = guide[0] + dx[0]
                guide[1] = guide[1] + dy[0]
        if kinput == 'down':
            if -width <= guide[0] + dx[1] <= width and -height <= guide[1] + dy[1] <= height:
                guide[0] = guide[0] + dx[1]
                guide[1] = guide[1] + dy[1]
        if kinput == 'left':
            if -width <= guide[0] + dx[2] <= width and -height <= guide[1] + dy[2] <= height:
                guide[0] = guide[0] + dx[2]
                guide[1] = guide[1] + dy[2]
        if kinput == 'right':
            if -width <= guide[0] + dx[3] <= width and -height <= guide[1] + dy[3] <= height:
                guide[0] = guide[0] + dx[3]
                guide[1] = guide[1] + dy[3]
    
    answer = guide
    return answer