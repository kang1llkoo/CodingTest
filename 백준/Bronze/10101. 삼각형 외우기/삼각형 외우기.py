a1 = int(input().strip())
a2 = int(input().strip())
a3 = int(input().strip())

triangle = [a1, a2, a3]

if sum(triangle) == 180:
    if a1 == a2 == a3 == 60:
        print("Equilateral")
    elif a1 == a2 or a2 == a3 or a3 == a1:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")