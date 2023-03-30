import sys

JH = sys.stdin.readline().rstrip()
mbti_dict = {}

for _ in range(int(sys.stdin.readline().rstrip())):
    mbti = sys.stdin.readline().rstrip()
    mbti_dict[mbti] = mbti_dict.get(mbti, 0) + 1

print(mbti_dict.get(JH, 0))