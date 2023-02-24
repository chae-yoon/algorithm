def solution(money):
    cup, change = divmod(money, 5500)
    answer = [cup, change]
    return answer