def solution(slice, n):
    answer = 0
    
    if n < slice:
        answer = 1
    else:
        answer = n // slice if n % slice == 0 else n // slice + 1
    
    return answer