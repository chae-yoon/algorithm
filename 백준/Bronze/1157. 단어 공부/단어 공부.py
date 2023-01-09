import sys

string = sys.stdin.readline().rstrip().lower()
char_dict = {}
max_char = []

for char in string:
    char_dict[char] = char_dict.get(char, 0) + 1
    
M = max(char_dict.values())

for key, value in char_dict.items():
    if value == M:
        max_char.append(key)

if len(max_char) == 1:
    print(max_char[0].upper())
else:
    print('?')