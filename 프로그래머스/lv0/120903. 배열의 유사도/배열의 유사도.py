def solution(s1, s2):
    answer = 0
    
    for s1_word in s1:
        for s2_word in s2:
            if s1_word == s2_word:
                answer +=1
    return answer