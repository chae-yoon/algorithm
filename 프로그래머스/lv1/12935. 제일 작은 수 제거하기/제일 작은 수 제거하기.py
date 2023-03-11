def solution(arr):
    answer = []
    
    min_num = min(arr)
    arr.remove(min_num)
    
    answer = arr if arr else [-1]
    
    return answer