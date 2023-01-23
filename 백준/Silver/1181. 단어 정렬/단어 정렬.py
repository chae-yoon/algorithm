import sys
from operator import itemgetter

N = int(sys.stdin.readline().rstrip())
words = [()]*N

for n in range(N):
    word = sys.stdin.readline().rstrip()
    word_tuple = (len(word), word)
    words[n] = tuple(word_tuple)

words_set = set(words)
words_sort = sorted(words_set, key= itemgetter(0,1))

for word in words_sort:
    print(word[1])