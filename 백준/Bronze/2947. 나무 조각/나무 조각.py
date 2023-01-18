nums = list(map(int, input().split()))
index = 0

while True:
    try:
        if nums[index] > nums[index + 1]:
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
            index += 1
            print(*nums)
        else:
            index += 1
    except:
        index = 0

    if nums == [1, 2, 3, 4, 5]:
        break