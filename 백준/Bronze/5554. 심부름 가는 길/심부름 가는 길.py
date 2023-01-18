import sys

move1 = int(sys.stdin.readline().rstrip())
move2 = int(sys.stdin.readline().rstrip())
move3 = int(sys.stdin.readline().rstrip())
move4 = int(sys.stdin.readline().rstrip())

M, S = divmod(sum([move1, move2, move3, move4]), 60)
print(M, S, sep='\n')