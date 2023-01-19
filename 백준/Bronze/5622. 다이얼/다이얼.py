sentence = input()

dialog = {}
start, result = 65, 0

for key in range(2, 10):
    jump = 4 if key == 7 or key == 9 else 3
    dialog[key] = dialog.get(key, list(map(chr, range(start, start + jump))))
    start += jump

for char in sentence:
    for key, value in dialog.items():
        if char in value:
            result += key

result += len(sentence)

print(result)