numbers = [int(input()) for n in range(7)]
odds = [number for number in numbers if number % 2 == 1]

if len(odds) > 0:
    print(sum(odds), min(odds), sep=('\n'))

else:
    print(-1)