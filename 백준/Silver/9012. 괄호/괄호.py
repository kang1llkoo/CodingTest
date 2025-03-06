import sys

n = int(sys.stdin.readline().strip())
tags = [sys.stdin.readline().strip() for _ in range(n)]

def vps(tag):
    stack = []
    for char in tag:
        if char == "(":  
            stack.append(char)
        elif char == ")":
            if not stack:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO" 

for tag in tags:
    print(vps(tag))