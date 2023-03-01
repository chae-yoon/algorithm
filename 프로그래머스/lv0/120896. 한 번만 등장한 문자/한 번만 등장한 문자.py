def solution(s):
    answer = ''
    words = []
    word_dict = {}
    
    for char in s:
        word_dict[char] = word_dict.get(char, 0) + 1
    
    for key, value in word_dict.items():
        if value == 1:
            words.append(key)
    
    words.sort()
    answer = ''.join(words)
    
    return answer