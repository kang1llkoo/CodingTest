import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    sentence = sys.stdin.readline().strip() 

    reversed_sentence = ' '.join(word[::-1] for word in sentence.split())
    print(reversed_sentence)