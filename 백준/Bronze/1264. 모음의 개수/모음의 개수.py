import sys

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    sentence = sys.stdin.readline().rstrip()
    vowel_count = 0

    if sentence == '#':
        break

    lower_sentence = sentence.lower()

    for v in vowels:
        vowel_count += lower_sentence.count(v)

    print(vowel_count)