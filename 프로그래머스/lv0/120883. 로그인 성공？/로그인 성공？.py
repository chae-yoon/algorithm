def solution(id_pw, db):
    answer = ''
    
    for data in db:
        if data[0] == id_pw[0] and data[1] == id_pw[1]:
            answer = 'login'
            break
        if data[0] == id_pw[0] and data[1] != id_pw[1]:
            answer = 'wrong pw'
            break
        else:
            answer = 'fail'
    
    return answer