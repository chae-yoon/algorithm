N = int(input())
scores = list(map(int, input().split()))
ctn, result = 0, 0

for score in scores:
    if score == 0:
        ctn = 0
    else:
        ctn += 1
    
    result += ctn

print(result)