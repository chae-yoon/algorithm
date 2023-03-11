def solution(s):
    answer = ''
    
    if len(s) % 2 == 1:
        middle = len(s) // 2
        answer = s[middle]
    else:
        middle = len(s) // 2 - 1
        answer = s[middle:middle+2]
    
    return answer