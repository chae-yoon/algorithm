while True:
    N = int(input())

    if N == 0:
        break

    result = [n for n in range(1, N + 1)]
    print(sum(result))