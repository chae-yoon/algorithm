def solution(lines):
    answer = 0
    plus = [0] * 101
    minus = [0] * 101
    
    for line in lines:
        for index in range(line[0], line[1]):
            if index < 0:
                minus[index] += 1
            else:
                plus[index] += 1
    
    for p in plus:
        if p > 1:
            answer += 1
    
    for m in minus:
        if m > 1:
            answer += 1
    
    return answer