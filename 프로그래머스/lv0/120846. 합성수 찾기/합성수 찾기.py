def solution(n):
    answer = 0
    
    for num in range(1, n+1):
        count = 0
        for g in range(2, num):
            if num % g == 0:
                count += 1
        if count >= 1:
            answer += 1
            
    return answer