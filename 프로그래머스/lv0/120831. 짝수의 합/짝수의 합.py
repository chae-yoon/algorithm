def solution(n):
    numbers = [num for num in range(n+1) if num % 2 == 0]
    answer = sum(numbers)
    return answer