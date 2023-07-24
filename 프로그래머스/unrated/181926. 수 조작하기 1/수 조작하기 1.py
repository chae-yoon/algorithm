def solution(n, control):
    control_dict = {
        "w" : 1,
        "s" : -1,
        "d" : 10,
        "a" : -10,
    }
    answer = n
    
    for c in control:
        answer += control_dict[c]
    
    return answer