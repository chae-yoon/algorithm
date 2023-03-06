def solution(spell, dic):
    answer = 2
    
    for word in dic:
        check = []
        for s in spell:
            if word.count(s) == 1:
                check.append(1)
        if sum(check) == len(spell):
            answer = 1
    
    return answer