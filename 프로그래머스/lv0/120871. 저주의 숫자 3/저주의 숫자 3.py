def solution(n):
    answer = 0
    start = 0
    
    while start != n:
        if answer % 3 == 0 or str(answer).count('3') > 0:
            answer += 1
            continue
        
        answer += 1
        start += 1

    answer -= 1  
        
    return answer