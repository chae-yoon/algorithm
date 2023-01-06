k, q, r, b, kn, p = map(int, input('').split(' '))

now = [k, q, r, b, kn, p]
original = [1, 1, 2, 2, 2, 8]
need = []

for i in range(len(now)):
    value = original[i] - now[i]
    need.append(str(value))

print(' '.join(need))