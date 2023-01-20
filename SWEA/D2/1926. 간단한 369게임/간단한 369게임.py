N = int(input())

numbers = list(range(1, N+1))
result = []

for number in numbers:
    n = 0

    for num in str(number):
        if num in ['3', '6', '9']:
            n += 1
    
    if n > 0:
        result.append('-' * n)
    
    else:
        result.append(number)
    
print(*result)