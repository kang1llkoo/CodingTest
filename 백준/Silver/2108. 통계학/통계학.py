import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
li = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])

nums_mean = round(sum(li) / n)
nums_median = li[n//2]

counter = Counter(li)
most_common = counter.most_common()

max_freq = most_common[0][1]
modes = [num for num, freq in most_common if freq == max_freq]

modes.sort()
nums_mode = modes[1] if len(modes) > 1 else modes[0]

nums_range = li[-1] - li[0]

print(nums_mean)
print(nums_median)
print(nums_mode)
print(nums_range)