from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    answer = []
    
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    
    answer = list(numbers)
    
    return answer