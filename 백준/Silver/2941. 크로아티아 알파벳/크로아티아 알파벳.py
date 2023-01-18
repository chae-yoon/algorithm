croatias = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
words = input()
word_count = 0

for croatia in croatias:
    if croatia in words:
        words = words.replace(croatia, '@')

word_count += words.count('@')
words = words.replace('@', '')
word_count += len(words)

print(word_count)