import sys

N = int(sys.stdin.readline().rstrip())
count = 0

if N < 10:
    a, b = 0, N
else:
    a, b = N//10, N%10


while True:
    c = (a + b) % 10
    count += 1
    if b * 10 + c == N:
        break

    a, b = b, c

print(count)