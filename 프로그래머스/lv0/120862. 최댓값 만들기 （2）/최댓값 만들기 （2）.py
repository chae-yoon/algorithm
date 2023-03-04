def solution(numbers):
    answer = 0
    multy = []
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            multy.append(numbers[i]*numbers[j])
    
    answer = max(multy)
    
    return answer