def solution(t, p):
    answer = 0
    num1 = int(p)

    for index in range(len(t)-len(p)+1):
        num2 = int(t[index:index+len(p)])

        if num2 <= num1:
            answer += 1

    return answer