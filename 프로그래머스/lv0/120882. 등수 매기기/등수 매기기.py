def solution(score):
    answer = []
    scores = []

    for s in score:
        scores.append(sum(s)/2)
    
    print(scores)
    sort_scores = sorted(scores, reverse=True)
    print(sort_scores)

    for s in scores:
        rank = sort_scores.index(s)+1
        answer.append(rank)
    
    return answer