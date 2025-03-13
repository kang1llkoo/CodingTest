import sys

arr = []
for i in range(5):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()
print(int(sum(arr)/len(arr)))
print(arr[len(arr)//2])