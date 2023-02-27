def solution(n):
    answer = []
    start = 2
    
    while start != n:
        if n % start == 0:
            n //= start
            answer.append(start)
            start = 2
        else:
            start += 1
    answer.append(start)
    answer = list(set(answer))
    answer.sort()
    
    return answer