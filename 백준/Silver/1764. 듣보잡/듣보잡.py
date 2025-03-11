n,m = map(int, input().split())
heard = set()
see = set()
result = []

for _ in range(n):
    heard.add(input())

for _ in range(m):
    see.add(input())

for i in heard:
    if i in see:
        result.append(i)

result.sort()
print(len(result))
for i in result:
    print(i)