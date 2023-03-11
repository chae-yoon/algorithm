def solution(arr, divisor):
    answer = []
    
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    
    answer.sort()
    
    if not answer:
        answer = [-1]
    
    return answer