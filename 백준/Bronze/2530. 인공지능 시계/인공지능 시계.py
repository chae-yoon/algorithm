import sys, datetime

H, M, S = map(int, sys.stdin.readline().split())
cooking = int(sys.stdin.readline().rstrip())

now_time = datetime.timedelta(hours=H, minutes=M, seconds=S)
cooking_time = datetime.timedelta(seconds=cooking)

finish_time = str(now_time + cooking_time)
finish_time = finish_time.split(',')[-1].split(':')
result = map(int, finish_time)

print(*result)