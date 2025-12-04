import math

def roots(a, b, c):
    if a == 0: 
        return "( )"
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        r1 = (-b + math.sqrt(discriminant)) / (2*a)
        r2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"({r1}, {r2})"
    elif discriminant == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        return "( )"

def value_y(a, b, c, x):
    return a*x**2 + b*x + c

def to_string(a, b, c):
    parts = [f"{a} * X^2"] if a != 0 else []
    if b != 0:
        parts.append(f"{b} * X")
    if c != 0:
        parts.append(f"{c}")
    return "f(x) = " + " + ".join(parts)

def derivation(a, b, c):
    parts = []
    if a != 0:
        parts.append(f"{2*a} * X")
    if b != 0:
        parts.append(f"{b}")
    if not parts:
        parts.append("0")
    return "f'(x) = " + " + ".join(parts)