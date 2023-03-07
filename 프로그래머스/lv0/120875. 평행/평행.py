from itertools import combinations

def solution(dots):
    answer = 0
    dot = list(combinations(dots, 2))
    for d in dot:
        lis = list(dots)

        lis.remove(d[0])
        lis.remove(d[1])

        increment1_x, increment1_y = d[1][0] - d[0][0], d[1][1] - d[0][1]
        increment2_x, increment2_y = lis[1][0] - lis[0][0], lis[1][1] - lis[0][1]

        if increment1_y / increment1_x == increment2_y / increment2_x:
            answer = 1

    return answer