import sys

sentence = sys.stdin.readline().rstrip()
happy = sentence.count(':-)')
sad = sentence.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')