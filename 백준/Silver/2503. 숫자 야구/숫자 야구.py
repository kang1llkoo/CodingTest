from itertools import permutations

# 입력
n = int(input())
questions = []
for _ in range(n):
    num, s, b = input().split()
    questions.append((num, int(s), int(b)))

candidates = list(permutations('123456789', 3))
count = 0

for candidate in candidates:
    is_possible = True
    candidate_str = ''.join(candidate)

    for q_num, q_strike, q_ball in questions:
        strike = 0
        ball = 0

        for i in range(3):
            if candidate_str[i] == q_num[i]:
                strike += 1
            elif candidate_str[i] in q_num:
                ball += 1

        if strike != q_strike or ball != q_ball:
            is_possible = False
            break

    if is_possible:
        count += 1

print(count)