T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    numbers.sort()
    numbers.pop(0)
    numbers.pop()

    average = round(sum(numbers) / len(numbers))

    print(f'#{test_case} {average}')