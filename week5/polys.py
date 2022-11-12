# poly1(x) + poly2(x)
def add_poly(poly1: list, poly2: list) -> list:
    size = max(len(poly1), len(poly2))
    poly_sum = [0 for i in range(size)]

    for i in range(len(poly1)):
        poly_sum[i] = poly1[i]

    for i in range(len(poly2)):
        poly_sum[i] += poly2[i]

    while poly_sum[-1] == 0 and len(poly_sum) > 1:
        poly_sum.pop()

    return poly_sum


# poly1(x) - poly2(x)
def sub_poly(poly1: list, poly2: list) -> list:
    size = max(len(poly1), len(poly2))
    poly_sub = [0 for i in range(size)]

    for i in range(len(poly1)):
        poly_sub[i] = poly1[i]

    for i in range(len(poly2)):
        poly_sub[i] -= poly2[i]

    while poly_sub[-1] == 0 and len(poly_sub) > 1:
        poly_sub.pop()

    return poly_sub


# poly1(x) * poly2(x)
def mul_poly(poly1: list, poly2: list) -> list:
    size = (len(poly1) + len(poly2) - 1)
    poly_mul = [0 for i in range(size)]

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            poly_mul[i + j] += poly1[i] * poly2[j]

    while poly_mul[-1] == 0 and len(poly_mul) > 1:
        poly_mul.pop()

    return poly_mul


# bool, [0], [0,0], itp.
def is_zero(poly: list) -> bool:
    return sum(poly) == 0


# poly1(x) == poly2(x)
def eq_poly(poly1: list, poly2: list) -> bool:
    for poly in [poly1, poly2]:
        while poly[-1] == 0 and len(poly) > 1:
            poly.pop()

    return poly1 == poly2


# poly(x0)
def eval_poly(poly: list, x0: float) -> float:
    poly.reverse()
    result = poly[0]

    for i in range(1, len(poly)):
        result = result * x0 + poly[i]

    return result


# poly1(poly2(x))
def combine_poly(poly1: list, poly2: list) -> list:
    result = [0]
    for i1, p1 in enumerate(poly1):
        result = add_poly(result, [p1 * el for el in pow_poly(poly2, i1)])
    return result


# poly(x) ** n
def pow_poly(poly: list, n: int) -> list:
    if n == 0:
        return [1]
    if n == 1:
        return poly
    result = poly.copy()
    for i in range(n-1):
        result = mul_poly(result, poly)
    return result


# pochodna wielomianu
def diff_poly(poly: list) -> list:
    result = []
    for i, x in enumerate(poly):
        if i == 0:
            continue
        result.append(i*x)
    return result