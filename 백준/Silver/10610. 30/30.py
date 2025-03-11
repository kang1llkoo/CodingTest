nums = input()
li = sorted(nums, reverse=True)
answer = ''.join(li)

if int(answer)%30 == 0:
    print(int(answer))
else:
    print(-1)