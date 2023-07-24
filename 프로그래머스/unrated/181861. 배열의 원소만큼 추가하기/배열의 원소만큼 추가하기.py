def solution(arr):
    answer = []
    for num in arr:
        for n in range(num):
            answer.append(num)
    return answer