def solution(n):
    answer = 0
    n = [n for n in str(n)]
    n.sort(reverse=True)
    answer = int(''.join(n))

    return answer