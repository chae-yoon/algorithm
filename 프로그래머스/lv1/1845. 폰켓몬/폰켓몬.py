def solution(nums):
    answer = 0
    nums_dict = {}
    
    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1
    pick = len(nums) // 2
    if len(nums_dict.keys()) >= pick:
        answer = pick
    else:
        answer = len(nums_dict.keys())
    return answer