import sys

N = int(sys.stdin.readline().rstrip())
record = {}

for n in range(N):
    name, status = sys.stdin.readline().split()

    if status == 'enter':
        record[name] = status
    
    else:
        record.pop(name, None)
    
print(*sorted(record.keys(), reverse=True), sep='\n')