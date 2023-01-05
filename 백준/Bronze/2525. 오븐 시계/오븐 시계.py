H, M = map(int, input('').split(' '))
times = int(input(''))

H += times // 60
M += times % 60

if M >= 60:
    H += 1
    M -= 60

if H >= 24:
    H -= 24

print(H, M)