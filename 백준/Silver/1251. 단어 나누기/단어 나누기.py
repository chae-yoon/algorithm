import sys, itertools

word = sys.stdin.readline().rstrip()

cbs = itertools.combinations(range(1, len(word)), 2)
indexs = list(cbs)
reverse_words = []

for index in indexs:
    reverse_word = word[:index[0]][::-1] + word[index[0]:index[1]][::-1] + word[index[1]:][::-1]
    reverse_words.append(reverse_word)

if not reverse_words:
    reverse_words.append(word)

print(sorted(reverse_words)[0])