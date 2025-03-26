lines = [input().strip() for _ in range(5)]

max_len = max(len(line) for line in lines)

result = []
for i in range(max_len):
    for j in range(5):
        if i < len(lines[j]):
            result.append(lines[j][i])

print("".join(result))