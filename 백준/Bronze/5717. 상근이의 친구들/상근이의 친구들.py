import sys

while True:
    boy, girl = map(int, sys.stdin.readline().split())

    if boy == 0 and girl == 0:
        break
    
    print(boy + girl)