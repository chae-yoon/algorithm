import sys

N = int(sys.stdin.readline().rstrip())
people = list(map(int, sys.stdin.readline().split()))
position = []
reject = 0

for person in people:
    if person in position:
        reject += 1
    else:
        position.append(person)

print(reject)