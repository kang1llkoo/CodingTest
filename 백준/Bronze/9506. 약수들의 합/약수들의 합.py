import sys

i = 1

while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    measure = []
    for i in range(1, n):
        if n % i == 0:
            measure.append(i)

    if sum(measure) == n:
        print(f"{n} = " + " + ".join(map(str, measure)))
    else:
        print(f"{n} is NOT perfect.")