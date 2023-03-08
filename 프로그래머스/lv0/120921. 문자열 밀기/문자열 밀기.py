from collections import deque

def solution(A, B):
    answer = 0
    if A == B:
        return 0

    A = deque(A)
    results = []
    
    rotation = 0
    while rotation != len(A)+1:
        A.rotate(1)
        rotation += 1

        if ''.join(A) == B:
            results.append(rotation)

    while rotation != len(A)+1:
        A.rotate(-1)
        rotation += 1

        if ''.join(A) == B:
            results.append(rotation)
        
    answer = min(results) if results else -1
    
    return answer