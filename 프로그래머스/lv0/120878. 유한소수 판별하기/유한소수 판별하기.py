def solution(a, b):
    answer = 0
    start = 2
    
    while start <= b:
        if a % start == 0 and b % start == 0:
            a //= start
            b //= start
            start = 2
        else:
            start += 1
    
    while b % 2 == 0:
        b //= 2
    
    while b % 5 == 0:
        b //= 5
    
    if b == 1:
        answer = 1
    else:
        answer = 2
    
    return answer