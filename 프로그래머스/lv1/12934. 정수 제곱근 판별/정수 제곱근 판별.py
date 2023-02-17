from math import sqrt

def solution(n):
    answer = 0
    start = 1
    while True:
        if start ** 2 == n:
            answer = (start+1) ** 2
            break
        if start ** 2 > n:
            answer = -1
            break
        start += 1
    return answer