from collections import Counter

n = input() 

count = Counter(n)  
count_6_9 = (count.get('6', 0) + count.get('9', 0) + 1) // 2 

max_count = max(count_6_9, max((count[c] for c in count if c not in {'6', '9'}), default=0))

print(max_count)