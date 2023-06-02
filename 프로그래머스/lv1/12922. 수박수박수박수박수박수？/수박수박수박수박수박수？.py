def solution(n):
    answer = ''
    n_multiply = n // 2

    if n % 2 == 0:
        answer = "수박" * n_multiply
    else:
        answer = "수박" * n_multiply + "수"
        
    return answer