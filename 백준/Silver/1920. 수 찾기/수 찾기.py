import sys

def binary_search(arr, x):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start+end) // 2

        if x == arr[mid]:
            return mid

        elif x > arr[mid]:
            start = mid + 1
        
        else:
            end = mid - 1
    
    return -1

N = int(sys.stdin.readline().rstrip())
An = list(map(int, sys.stdin.readline().split()))
An.sort()

M = int(sys.stdin.readline().rstrip())
Mn = list(map(int, sys.stdin.readline().split()))

for m in Mn:
    print(1 if binary_search(An, m) != -1 else 0)