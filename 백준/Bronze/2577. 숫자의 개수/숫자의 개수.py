number = 1

for n in range(3):
    number *= int(input())

str_number = str(number)

for n in range(10):
    print(str_number.count(str(n)))