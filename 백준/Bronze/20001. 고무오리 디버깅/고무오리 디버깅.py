import sys

sys.stdin.readline().rstrip()
commands = []

while True:
    command = sys.stdin.readline().rstrip()

    if command == '고무오리 디버깅 끝':
        break

    if command == '문제':
        commands.append(0)
    
    if command == '고무오리':
        if len(commands) == 0:
            commands.append(0)
            commands.append(0)
        else:
            commands.pop()

print('고무오리야 사랑해' if len(commands) == 0 else '힝구')