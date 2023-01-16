scores = 0

for t in range(5):
    score = int(input())

    if score < 40:
        scores += 40
    else:
        scores += score

print(scores//5)