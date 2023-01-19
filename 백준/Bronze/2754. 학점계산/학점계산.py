c_score = {
    'A' : 4.0,
    'B' : 3.0,
    'C' : 2.0,
    'D' : 1.0,
    'F' : 0.0,
    '+' : 0.3,
    '-' : -0.3,
}

scores = input()
result = [c_score.get(score, 0) for score in scores]

print(sum(result))