ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

b = [cx - az, cy // ay,  cz - ax] 

print(*b)