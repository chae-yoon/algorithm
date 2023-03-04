def solution(my_str, n):
    answer = []
    word = ''
    count = 0
    
    for index in range(len(my_str)):
        word += my_str[index]
        count += 1

        if count % n == 0:
            answer.append(word)
            word = ''
            count = 0
    
    if word != '':
        answer.append(word)
    
    return answer