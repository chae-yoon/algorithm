def solution(emergency):
    orders = sorted(emergency, reverse=True)
    answer = [orders.index(e)+1 for e in emergency]
    return answer