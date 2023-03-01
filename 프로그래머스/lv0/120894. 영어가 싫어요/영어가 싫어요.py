word_dict = {
    'zero' : "0", 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'
}

def solution(numbers):
    answer = ''
    word = numbers[0]
    
    for char in numbers[1:]:
        try:
            answer += word_dict[word]
            word = char
        except:
            word += char
            
    answer += word_dict[word]
    answer = int(answer)
    
    return answer