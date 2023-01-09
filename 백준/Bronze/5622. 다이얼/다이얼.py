import sys

num_dict = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
}

min_time = 0
word = sys.stdin.readline().rstrip()

for c in word:
    for k, v in num_dict.items():
        if c in v:
            min_time += k

min_time += len(word)

print(min_time)