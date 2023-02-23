def solution(n):
    answer = 1
    num, pizza = 2, 6
    guide = 6 if n > 6 else n
    
    while num <= guide:
        if pizza % num == 0 and n % num == 0:
            answer *= num
            pizza //= num
            n //= num
            num = 2
        else:
            num += 1
    
    answer = answer * pizza * n // 6
    
    return answer