def solution(sides):
    answer = 0
    side = []

    for num in range(abs(sides[0] - sides[1])+1, max(sides)):
        side.append(num)
    
    for num in range(max(sides), sum(sides)):
        side.append(num)
    
    side = set(side)
    answer = len(side)
    
    return answer