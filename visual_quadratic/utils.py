def get_roots(a: int, b: int, c: int):
    if a == 0 and b == 0 and c == 0:
        return []
    D = b**2 - 4*a*c
    if D == 0:
        roots = [-b / (2*a)]
    elif D > 0:
        roots = [(-b - D**0.5) / (2*a), (-b + D**0.5) / (2*a)]
    else:
        roots = []
    return roots