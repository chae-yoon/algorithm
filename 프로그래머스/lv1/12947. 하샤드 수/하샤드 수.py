def solution(x):
    answer = False
    divide_nums = [int(num) for num in str(x)]
    if x % sum(divide_nums) == 0:
        answer = True
    return answer