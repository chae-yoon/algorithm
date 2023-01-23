import sys

x, y, w, h = map(int, sys.stdin.readline().split())

if x > w / 2:
    time1 = w - x

else:
    time1 = x

if y > h / 2:
    time2 = h - y

else:
    time2 = y

print(min(time1,time2))