def solution(num):
    answer = 0
    
    for _ in range(500):
        if num == 1:
            answer = _
            break
        
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3 + 1
    else:
        answer = -1
    
    
    return answer