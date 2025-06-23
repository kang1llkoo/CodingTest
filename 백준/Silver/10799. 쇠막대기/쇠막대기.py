import sys

string = sys.stdin.readline().strip()
stack = []
result = 0

for i in range(len(string)):
    if string[i] == '(':
        stack.append('(')
    else:  # ')'
        stack.pop()
        if string[i - 1] == '(':  # 레이저
            result += len(stack)
        else:  # 막대기 끝
            result += 1

print(result)