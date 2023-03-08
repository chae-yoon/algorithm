def solution(before, after):
    answer = 0
    before_dict, after_dict = {}, {}

    for char in before:
        before_dict[char] = before_dict.get(char, 0) + 1

    for char in after:
        after_dict[char] = after_dict.get(char, 0) + 1

    if before_dict == after_dict:
        answer = 1

    return answer