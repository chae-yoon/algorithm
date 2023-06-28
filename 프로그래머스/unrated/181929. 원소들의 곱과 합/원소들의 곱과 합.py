def solution(num_list):
    m = 1
    for num in num_list:
        m *= num
    answer = 0 if m > sum(num_list) ** 2 else 1
    return answer