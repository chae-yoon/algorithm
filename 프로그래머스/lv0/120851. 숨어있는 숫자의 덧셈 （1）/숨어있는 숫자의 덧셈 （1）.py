def solution(my_string):
    answer = 0
    answers = []
    for char in my_string:
        try:
            answers.append(int(char))
        except:
            pass
    answer = sum(answers)
    return answer