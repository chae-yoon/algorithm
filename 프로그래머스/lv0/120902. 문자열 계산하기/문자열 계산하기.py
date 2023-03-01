def solution(my_string):
    answer = 0
    words = my_string.split()
    answer = int(words[0])
    
    for index in range(0,len(words)-1,2):
        if words[index+1] == "+":
            answer += int(words[index+2])
        elif words[index+1] == '-':
            answer -= int(words[index+2])
    
    return answer