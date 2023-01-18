syllables = list(map(int, input().split()))

syllables_ascending = sorted(syllables)
syllables_descending = sorted(syllables, reverse=True)

if syllables == syllables_ascending:
    print('ascending')
elif syllables == syllables_descending:
    print('descending')
else:
    print('mixed')