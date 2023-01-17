width = []
height = []

for i in range(3):
    w, h = map(int, input().split())
    width.append(w)
    height.append(h)

width.sort()
height.sort()

new_width = width[2] if width[0] == width[1] else width[0]
new_height = height[2] if height[0] == height[1] else height[0]

print(new_width, new_height)