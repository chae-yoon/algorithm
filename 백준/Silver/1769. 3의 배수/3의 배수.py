import sys

number = sys.stdin.readline().rstrip()
cicle = 0

while int(number) >= 10:
    result = sum(list(map(int, number)))
    number = str(result) 

    cicle += 1

print(cicle)
print('YES' if int(number) % 3 == 0 else 'NO')