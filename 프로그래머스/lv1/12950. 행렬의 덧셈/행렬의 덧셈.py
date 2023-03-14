def solution(arr1, arr2):
    answer = []
    
    for index in range(len(arr1)):
        ar1 = arr1[index]
        ar2 = arr2[index]
        ans = []
        for i in range(len(ar1)):
            ans.append(ar1[i]+ar2[i])
        answer.append(ans)
    
    return answer