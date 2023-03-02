def solution(num, k):
    num = str(num)
    answer = num.find(str(k)) + 1 if num.find(str(k)) != -1 else -1
    return answer