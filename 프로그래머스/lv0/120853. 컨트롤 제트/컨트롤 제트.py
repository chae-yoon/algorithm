def solution(s):
    string = s.split()
    answer = 0
    
    for index in range(len(string)-1):
        if string[index+1] == 'Z':
            continue
            
        if string[index] == 'Z':
            continue
        
        answer += int(string[index])
    
    answer += int(string[-1]) if string[-1] != 'Z' else 0
    
    return answer