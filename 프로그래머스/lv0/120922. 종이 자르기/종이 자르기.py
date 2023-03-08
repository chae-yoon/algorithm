def solution(M, N):
    answer = 0
    
    max_num = max([M, N])
    min_num = min([M, N])
    
    answer += max_num - 1
    answer += (min_num - 1) * max_num
    
    return answer