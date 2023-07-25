def solution(my_string, is_prefix):
    answer = 0
    
    if len(my_string) < len(is_prefix):
        return answer
    
    for index, string in enumerate(is_prefix):
        if string != my_string[index]:
            break
    else:
        answer = 1
    return answer