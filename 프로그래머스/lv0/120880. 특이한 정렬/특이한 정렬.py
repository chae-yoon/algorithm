def solution(numlist, n):
    answer = []
    abs_num = []

    for num in numlist:
        abs_num.append((num, abs(num-n)))

    abs_num.sort(key= lambda x:(x[1], -x[0]))
    
    for num in abs_num:
        answer.append(num[0])
    return answer