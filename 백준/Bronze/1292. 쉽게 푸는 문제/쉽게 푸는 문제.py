a, b = map(int, input().split())
# a: 구간의 시작
# b: 구간의 끝

list = [0]

for i in range(1, 100):
    for j in range(i):
        list.append(i)
    if len(list) > 1000:
        break

print(sum(list[a:b+1]))