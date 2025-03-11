nums = list(map(int,input().split()))
max_num = max(nums)
nums.remove(max_num)
print(max(nums))