def solution(my_string):
    ans = []
    
    for char in my_string:
        if char not in ans:
            ans.append(char)
    
    answer = ''.join(ans)
    return answer