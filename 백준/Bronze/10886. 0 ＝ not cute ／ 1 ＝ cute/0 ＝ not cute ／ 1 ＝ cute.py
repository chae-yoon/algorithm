N = int(input())
opinion = 0

for n in range(N):
    opinion += int(input())

if opinion > N/2:
    print('Junhee is cute!')

else:
    print('Junhee is not cute!')