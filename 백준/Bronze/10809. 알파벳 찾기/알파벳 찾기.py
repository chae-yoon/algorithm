word = input()
answer = []

for c in range(97, 123):
    answer.append(word.find(chr(c)))

print(*answer)