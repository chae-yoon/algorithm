import math

def solution(balls, share):
    answer = 0
    np = math.factorial(balls)
    nmp = math.factorial(balls-share)
    mp = math.factorial(share)
    answer = np // (nmp*mp)
    return answer