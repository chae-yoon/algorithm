import sys

string = sys.stdin.readline().rstrip()

if int(string[:2]) > 10:
    A = int(string[0])
    B = int(string[1:])

else:
    A = int(string[0:2])
    B = int(string[2:])

print(A + B)