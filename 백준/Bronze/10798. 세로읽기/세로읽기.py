import sys

word_dict = {
    'length' : [],
}

for i in range(5):
    word_dict[i] = sys.stdin.readline().rstrip()
    word_dict['length'].append(len(word_dict[i]))

string = ''

for j in range(max(word_dict['length'])):
    for i in range(5):
        try:
            string += word_dict[i][j]
        except:
            string += ''
    
print(string)