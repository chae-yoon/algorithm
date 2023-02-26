wins = {'2': '0', '0': '5', '5': '2'}

def solution(rsp):
    answer = ''
    
    for letter in rsp:
        answer += wins[letter]
    
    return answer