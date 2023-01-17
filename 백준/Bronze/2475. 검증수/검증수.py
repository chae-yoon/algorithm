numbers = list(map(int, input().split()))

add_number = 0

for number in numbers:
    add_number += number ** 2

print(add_number % 10)