import sys

N = int(sys.stdin.readline().rstrip())
N_list = list(map(int, sys.stdin.readline().split()))
N_dict = {}

for n in N_list:
    N_dict[n] = N_dict.get(n, 0) + 1

M = int(sys.stdin.readline().rstrip())
M_list = list(map(int, sys.stdin.readline().split()))

result = [N_dict.get(n, 0) for n in M_list]
print(*result)