from collections import Counter

def solution(array):
    answer = 0
    count_array = Counter(array).most_common()
    
    if len(count_array) == 1:
        answer = count_array[0][0]
    else:
        if count_array[0][1] == count_array[1][1]:
            answer = -1
        else:
            answer = count_array[0][0]
            
    return answer