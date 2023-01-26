import sys

N = int(sys.stdin.readline().rstrip())
dict_num = {}

for n in range(N):
    num = int(sys.stdin.readline().rstrip())
    dict_num[num] = dict_num.get(num, 0) + 1

sort_key = sorted(dict_num.keys())

for key in sort_key:
    for n in range(dict_num.get(key)):
        print(key)