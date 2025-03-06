import sys

n = int(sys.stdin.readline().strip())

test_cases = [sys.stdin.readline().strip() for _ in range(n)]

for test in test_cases:
    score = 0
    current_score = 0
    for char in test:
        if char == 'O':
            current_score += 1
            score += current_score
        else:
            current_score = 0
    print(score)