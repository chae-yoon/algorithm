words = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    answer = 0
    
    for bab in babbling:
        for word in words:
            bab = bab.replace(word, '-', 1)
        
        bab = bab.replace('-', '')
        
        if bab == '':
            answer += 1
    
    return answer