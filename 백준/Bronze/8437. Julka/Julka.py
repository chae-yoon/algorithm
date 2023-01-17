import sys

apples = int(sys.stdin.readline().rstrip())
more = int(sys.stdin.readline().rstrip())

print((apples - more) // 2 + more, (apples - more) // 2, sep='\n')