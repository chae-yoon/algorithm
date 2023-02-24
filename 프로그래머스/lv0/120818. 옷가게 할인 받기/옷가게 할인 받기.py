def solution(price):
    answer = 0
    
    if price >= 500000:
        answer = int(price * .8)
    elif price >= 300000:
        answer = int(price * .9)
    elif price >= 100000:
        answer = int(price * .95)
    else:
        answer = price
    
    return answer