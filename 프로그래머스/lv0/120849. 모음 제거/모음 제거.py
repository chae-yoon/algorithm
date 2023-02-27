vowels = ['a', 'e', 'i', 'o', 'u']

def solution(my_string):
    answer = ''
    
    for char in my_string:
        if char not in vowels:
            answer += char
    
    return answer