def solution(polynomial):
    answer = ''
    x = 0
    a = 0
    
    nums = polynomial.split()
    nums = [num for num in nums if num != '+']
    
    for num in nums:
        if num[-1] == 'x':
            if len(num) == 1:
                x += 1
            else:
                x += int(num[:-1])
        else:
            a += int(num)
    
    if x != 0 and a != 0:
        if x == 1:
            answer = f'x + {a}'
        else:
            answer = f'{x}x + {a}'
    elif x == 0 and a != 0:
        answer = f'{a}'
    elif x != 0 and a == 0:
        if x == 1:
            answer = f'x'
        else:
            answer = f'{x}x'
    
    return answer