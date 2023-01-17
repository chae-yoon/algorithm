T = int(input())

for t in range(T):
    lt, wt, le, we = map(int, input().split())

    if lt * wt > le * we:
        winner = 'TelecomParisTech'

    elif lt * wt == le * we:
        winner = 'Tie'

    else:
        winner = 'Eurecom'

    print(winner)