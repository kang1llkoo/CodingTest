from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    unique_num = set()
    for length in range(1, len(numbers)+1):
        for perm in permutations(numbers, length):
            num = int(''.join(perm))
            unique_num.add(num)
    prime_count = sum(1 for num in unique_num if is_prime(num))
    return prime_count