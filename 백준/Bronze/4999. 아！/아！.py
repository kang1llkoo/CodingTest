import sys

input = sys.stdin.readline

jw_max = input().strip()
dr_want = input().strip()

if len(jw_max) < len(dr_want):
    print("no")
else:
    print("go")