def solution(numbers):
    numbers.sort()
    num1 = numbers.pop()
    num2 = numbers.pop()
    answer = num1 * num2
    return answer