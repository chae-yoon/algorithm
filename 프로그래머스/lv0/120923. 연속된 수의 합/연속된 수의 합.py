def solution(num, total):
    answer = []
    
    if num % 2 == 1:
        guide = total // num
        answer.append(guide)
        for index in range(1, num // 2+1):
            answer.append(guide+index)
            answer.append(guide-index)
    else:
        index = -100
        while True:
            if sum(answer) == total:
                break
            answer = list(range(index, index+num))
            index += 1
    
    answer.sort()
    
    return answer