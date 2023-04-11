import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    string = sys.stdin.readline().rstrip()
    new_string = string[0].upper() + string[1:]
    print(new_string)