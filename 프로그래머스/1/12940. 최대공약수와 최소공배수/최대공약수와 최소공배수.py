import math

def solution(n, m):
    gcd = math.gcd(n,m)
    return [gcd, int(n*m/gcd)]
        