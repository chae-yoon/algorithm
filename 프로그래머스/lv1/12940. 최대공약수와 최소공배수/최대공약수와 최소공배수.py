import math

def solution(n, m):
    answer = []
    gcd_num = math.gcd(n, m)
    lcm_num = gcd_num * (n // gcd_num) * (m // gcd_num)
    answer = [gcd_num, lcm_num]
    return answer