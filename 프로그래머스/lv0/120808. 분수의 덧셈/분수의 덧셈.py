def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1
    x = 2
    
    while x <= denom:
        if denom % x == 0 and numer % x == 0:
            denom //= x
            numer //= x
            x = 2
        else:
            x += 1            
        
    answer = [numer, denom]
    
    return answer