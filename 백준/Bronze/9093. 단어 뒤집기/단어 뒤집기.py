T = int(input())

for t in range(T):
    words = input().split()
    sentence = []

    for word in words:
       sentence.append(word[::-1])

    print(*sentence)