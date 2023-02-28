def solution(array, n):
    array.sort()
    answer = array[0]
    step = abs(n-array[0])
    
    for num in array:
        if abs(n-num) < step:
            if num > answer:
                answer = num
                step = n-num
        
    return answer