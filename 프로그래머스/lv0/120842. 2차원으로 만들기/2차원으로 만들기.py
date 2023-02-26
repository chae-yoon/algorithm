def solution(num_list, n):
    answer = [num_list[num*n:num*n+n] for num in range(len(num_list)//n)]
    return answer