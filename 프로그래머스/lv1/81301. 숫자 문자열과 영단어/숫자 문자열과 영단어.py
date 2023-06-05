str_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def solution(s):
    answer = ''
    for value, str_num in enumerate(str_nums):
        s = s.replace(str_num, str(value))
    answer = int(s)
    return answer