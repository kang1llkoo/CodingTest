t = int(input())

a = 300 
b = 60 
c = 10
count = 0

count_a = t // a
t %= a

count_b = t // b
t %= b

count_c = t // c
t %= c

if t != 0:
    print(-1)
else:
    print(count_a, count_b, count_c)