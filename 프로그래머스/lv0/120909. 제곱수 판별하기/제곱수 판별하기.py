def solution(n):
    answer = 2
    for num in range(1, n):
        if num ** 2 > n:
            break
        
        if num ** 2 == n:
            answer = 1
    return answer