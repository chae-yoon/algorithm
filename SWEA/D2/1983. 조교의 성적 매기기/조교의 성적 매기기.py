T = int(input())
scores = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T+1):
    students, K = map(int, input().split())
    score = {}

    for student in range(1, students+1):
        middle_exam, last_exam, assignment = map(int, input().split())
        result = middle_exam * .35 + last_exam * .45 + assignment * .2

        score[student] = result
        
    sort_score = sorted(score, key= lambda x: score[x], reverse=True)
    K_score = sort_score.index(K)

    num = {k: list(range(i*(students//10)+1, i*(students//10)+students//10+1)) for i, k in enumerate(scores) }

    for k,v in num.items():
        if K_score+1 in v:
            result = k
            break

    print(f'#{test_case} {result}')