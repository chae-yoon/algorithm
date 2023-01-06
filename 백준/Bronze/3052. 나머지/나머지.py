import sys

num_list = []

for i in range(10):
    value = int(sys.stdin.readline().rstrip())
    num_list.append(value % 42)
    
print(len(set(num_list)))