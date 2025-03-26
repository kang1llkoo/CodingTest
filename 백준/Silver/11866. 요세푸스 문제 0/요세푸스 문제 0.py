n, k = map(int, input().split())

li = [i for i in range(1, n+1)]
result = []
idx = 0

while li:
    idx = (idx + k - 1) % len(li)
    result.append(li.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")