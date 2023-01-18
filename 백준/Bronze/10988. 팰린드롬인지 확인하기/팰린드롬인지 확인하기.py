strings = input()
is_palindrome = 1

for n in range(len(strings)//2):
    if strings[n] == strings[len(strings)-n-1]:
        pass
    else:
        is_palindrome = 0
        break

print(is_palindrome)