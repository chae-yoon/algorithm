num1 = int(input(''))
num2 = input('')

for i in range(0,len(num2)):
    print(f'{num1 * int(num2[2-i])}')

print(f'{num1 * int(num2)}')