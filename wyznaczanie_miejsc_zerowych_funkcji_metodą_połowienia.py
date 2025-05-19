
def f(x: float) -> float:
    return (x - 2) * (x - 11)


def zero(a: float, b: float) -> float:
    while b - a  >= 0.01:
        fa = f(a)
        fb = f(b)
        middle = (a + b) / 2
        fm = f(middle)
        if fm == 0:
            return middle
        if fa > 0 and fm < 0 and fb < 0:
            b = middle
        elif fa > 0 and fm > 0 and fb < 0:
            a = middle
        elif fa < 0 and fm > 0 and fb > 0:
            b = middle
        else:
            a = middle

    return (a + b) / 2


print(zero(0, 10))