# 해시, 딕셔너리

import sys
input = sys.stdin.read

data = input().splitlines()
n, m = map(int, data[0].split())

dict_name_to_num = {}
dict_num_to_name = {}

for i in range(1, n+1):
    name = data[i]
    dict_name_to_num[name] = i
    dict_num_to_name[i] = name

result = []
for j in range(n+1, n+1+m):
    query = data[j]
    if query.isdigit():
        result.append(dict_num_to_name[int(query)])
    else:
        result.append(str(dict_name_to_num[query]))

print('\n'.join(result))