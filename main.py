from typing import Tuple

# Algoritmo de Karatsuba
def karatsuba(x: int, y: int) -> int:

    if x == 0 or y == 0:
        return 0
    if abs(x) < 10 or abs(y) < 10:
        return x * y
    
    n = max(len(str(abs(x))), len(str(abs(y))))
    m = n // 2
    base = 10 ** m

    ax, bx = divmod(abs(x), base)
    ay, by = divmod(abs(y), base)
    ac = karatsuba(ax, ay)
    bd = karatsuba(bx, by)
    ad_bc = karatsuba(ax + bx, ay + by) - ac - bd
    result = ac * (10 ** (2 * m)) + ad_bc * base + bd
    sign = -1 if ((x < 0) ^ (y < 0)) else 1

    return sign * result


if __name__ == "__main__":

    a = 12345678901234567890
    b = 98765432109876543210
    
    print(karatsuba(a, b))
