def solution(a, b):
    answer = ''
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = sum([day for day in month_day[:a]]) + b
    answer = day_of_week[days%7 - 1]
    return answer