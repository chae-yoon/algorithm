def d(n):
    str_num = str(n)
    result = n

    for c in str_num:
        result += int(c)
    
    return result

lis = list(range(1, 10001))

for i in range(1, 10001):
    try:
        lis.remove(d(i))
    except:
        pass

print(*lis, sep='\n')