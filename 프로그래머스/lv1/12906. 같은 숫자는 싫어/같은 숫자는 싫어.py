def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    prior = arr[0]
    answer.append(prior)
    for num in arr[1:]:
        if num != prior:
            answer.append(num)
            prior = num
    return answer