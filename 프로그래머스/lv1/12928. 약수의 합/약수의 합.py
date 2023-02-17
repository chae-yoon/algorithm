def solution(n):
    answer = 0
    for nums in range(1, n+1):
        if n % nums == 0:
            answer += nums
    
    return answer