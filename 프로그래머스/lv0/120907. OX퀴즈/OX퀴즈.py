def solution(quiz):
    answer = []
    
    for q in quiz:
        solve = ''
        sentence = q.split()
        
        if sentence[1] == '+':
            if int(sentence[0]) + int(sentence[2]) == int(sentence[4]):
                solve = 'O'
            else:
                solve = 'X'
        
        if sentence[1] == '-':
            if int(sentence[0]) - int(sentence[2]) == int(sentence[4]):
                solve = 'O'
            else:
                solve = 'X'
        answer.append(solve)
    
    return answer