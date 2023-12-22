def solution(a, b):
    if a % 2 != 0:
        if b % 2 != 0:
            return a**2 + b**2
        elif b % 2 == 0:
            return 2 * (a + b)
    elif a % 2 == 0:
        if b % 2 != 0:
            return 2 * (a + b)
        elif b % 2 == 0:
            return abs(a - b)


