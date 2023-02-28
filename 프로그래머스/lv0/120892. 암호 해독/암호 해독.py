def solution(cipher, code):
    answer = ''
    
    for n in range(len(cipher)//code):
        answer += cipher[code*n + code -1]
    
    return answer