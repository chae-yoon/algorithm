def solution(array, n):
    answer = 0
    array_dict = {}
    
    for num in array:
        array_dict[num] = array_dict.get(num, 0) + 1
    
    answer = array_dict.get(n, 0)
    
    return answer