def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    p_count = s.lower().count('p')
    y_count = s.lower().count('y')
    
    if p_count != y_count:
        answer = False
    
    return answer