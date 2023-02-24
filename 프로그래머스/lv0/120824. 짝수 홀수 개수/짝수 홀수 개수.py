def solution(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    answer = [len(evens), len(num_list)-len(evens)]
    return answer