def solution(myString, pat):
    answer = 1 if myString.lower().find(pat.lower()) != -1 else 0
    return answer