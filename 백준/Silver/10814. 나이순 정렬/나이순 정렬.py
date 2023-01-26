import sys
from operator import itemgetter

N = int(sys.stdin.readline().rstrip())
users = []

for n in range(N):
    age, name = sys.stdin.readline().split()
    users.append(tuple([n, int(age), name]))

sort_user = sorted(users, key= itemgetter(1,0))

for user in sort_user:
    print(user[1], user[2])