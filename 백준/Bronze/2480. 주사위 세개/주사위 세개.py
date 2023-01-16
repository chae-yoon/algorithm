dice = list(map(int, input().split()))
set_dice = set(dice)

if len(set_dice) == 1:
    price = 10000 + set_dice.pop() * 1000

elif len(set_dice) == 3:
    dice.sort()
    price = dice.pop() * 100

else:
    dice.sort()
    
    if dice[0] == dice[1]:
        price = 1000 + dice[0] * 100

    else:
        price = 1000 + dice[1] * 100

print(price)