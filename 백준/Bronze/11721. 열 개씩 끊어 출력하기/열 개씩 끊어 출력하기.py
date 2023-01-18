words = input()

for index in range(len(words) // 10 if len(words) % 10 == 0 else len(words) // 10 + 1):
    try:
        print(words[index * 10:(index + 1) * 10])
    except:
        print(words[index * 10:])