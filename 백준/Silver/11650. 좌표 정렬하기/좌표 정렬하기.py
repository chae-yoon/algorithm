import sys
from operator import itemgetter

N = int(sys.stdin.readline().rstrip())
coordinates = [()]*N

for n in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates[n] = (x, y)

coordinates_sort = sorted(coordinates, key= itemgetter(0,1))

for coordinate in coordinates_sort:
    print(*coordinate)