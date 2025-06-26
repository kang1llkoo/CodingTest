import sys
input = sys.stdin.readline

n = int(input())
cards = set(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

result = ['1' if target in cards else '0' for target in targets]


print(' '.join(result))