import sys, itertools

N = sys.stdin.readline().rstrip()

N_num = int(N)
nums = ['4', '7'] * len(N)
result = 0

for _ in range(len(N)-1 ,len(N)+1):
    numbers = set(itertools.combinations(nums, _))
    
    for number in numbers:
        int_number = int(''.join(list(number))) if len(number) > 0 else 0
        if int_number <= N_num and int_number > result:
            result = int_number

print(result)