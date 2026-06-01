def karatsuba(x: int, y: int) -> int:
    """
    Multiplication using Karatsuba algorithm.
    """

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    high1 = x // (10 ** m)
    low1 = x % (10 ** m)

    high2 = y // (10 ** m)
    low2 = y % (10 ** m)

    z0 = karatsuba(low1, low2)
    z2 = karatsuba(high1, high2)
    z1 = karatsuba(low1 + high1, low2 + high2) - z0 - z2

    return z2 * (10 ** (2 * m)) + z1 * (10 ** m) + z0


if __name__ == "__main__":
    a = 12345678
    b = 87654321

    print("Karatsuba:", karatsuba(a, b))
    print("Python:", a * b)