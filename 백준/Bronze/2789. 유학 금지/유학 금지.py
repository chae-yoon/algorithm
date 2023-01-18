A = 'CAMBRIDGE'
strings = input()

for a in A:
    if a in strings:
        strings = strings.replace(a, '')
    
print(strings)