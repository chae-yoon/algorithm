def solution(s):
    strings = list(s)
    strings.sort(reverse=True)
    answer = ''.join(strings)
    return answer