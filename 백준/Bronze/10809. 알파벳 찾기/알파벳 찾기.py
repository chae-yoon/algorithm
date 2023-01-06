S = input('')

dic = {}

for i in range(97, 123):
    dic[i] = -1

for char in S:
    if dic[ord(char)] < 0:
        dic[ord(char)] = S.index(char)
    else:
        continue

lis = map(str, list(dic.values()))

print(' '.join(lis))