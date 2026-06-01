def karatsuba(x: int, y: int) -> int:
    """
    Алгоритм умножения Карацубы.
    """

    sign = 1

    if x < 0:
        sign *= -1
        x = abs(x)

    if y < 0:
        sign *= -1
        y = abs(y)

    result = _karatsuba_recursive(x, y)

    return sign * result


def _karatsuba_recursive(x: int, y: int) -> int:

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // (10**m)
    b = x % (10**m)

    c = y // (10**m)
    d = y % (10**m)

    z0 = _karatsuba_recursive(b, d)

    z2 = _karatsuba_recursive(a, c)

    z1 = (_karatsuba_recursive(a + b, c + d) - z2 - z0)

    return (z2 * (10 ** (2 * m)) + z1 * (10**m) + z0)


class KaratsubaCounter:

    def __init__(self):
        self.calls = 0

    def multiply(self, x: int, y: int) -> int:
        self.calls = 0
        return self._multiply(x, y)

    def _multiply(self, x: int, y: int) -> int:

        self.calls += 1

        if x < 10 or y < 10:
            return x * y

        n = max(len(str(x)), len(str(y)))
        m = n // 2

        a = x // (10**m)
        b = x % (10**m)

        c = y // (10**m)
        d = y % (10**m)

        z0 = self._multiply(b, d)
        z2 = self._multiply(a, c)

        z1 = (self._multiply(a + b, c + d) - z0 - z2)

        return (z2 * (10 ** (2 * m)) + z1 * (10**m) + z0)


if __name__ == "__main__":

    a = 12345678
    b = 87654321

    print("Карацуба:", karatsuba(a, b))
    print("Python:", a * b)
