def solution(n):
    answer = 1
    result = 1
    
    while result <= n:
        result *= answer
        answer += 1
    
    answer -= 2
    
    return answer