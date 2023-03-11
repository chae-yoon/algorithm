def solution(numbers):
    nums = set(range(10))
    numbers = set(numbers)

    results = nums - numbers
    results = list(results)

    answer = sum(results)
    
    return answer