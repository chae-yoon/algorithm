def solution(num_list):
    answer = 0
    for index, num in enumerate(num_list):
        if num < 0:
            answer = index
            break
    else:
       answer = -1     
        
    return answer