import sys, datetime


for n in range(3):
    work_time = list(map(int, sys.stdin.readline().split()))

    start_time = datetime.timedelta(hours=work_time[0], minutes=work_time[1], seconds=work_time[2])
    end_time = datetime.timedelta(hours=work_time[3], minutes=work_time[4], seconds=work_time[5])

    working = str(end_time - start_time)
    work_times = map(int, working.split(':'))

    print(*work_times)