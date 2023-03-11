def solution(s):
    answer = False
    
    if len(s) == 4 or len(s) == 6:
        try:
            for num in s:
                a = int(num)
            answer = True
        except:
            return answer
    
    return answer