score = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}

total_score = 0
total_result = 0

for _ in range(20):
    subject, result, grad = input().split()
    result = float(result)

    if grad == 'P':
        continue

    total_score += result * score[grad]
    total_result += result

gpa = total_score / total_result
print(f"{gpa:.6f}")