def karatsuba(x: int, y: int) -> int:
    """
    Алгоритм умножения Карацубы с использованием бинарных сдвигов.
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
    if x < 16 or y < 16:
        return x * y

    n = max(x.bit_length(), y.bit_length())
    m = n // 2

    a = x >> m
    b = x & ((1 << m) - 1)

    c = y >> m
    d = y & ((1 << m) - 1)

    z0 = _karatsuba_recursive(b, d)
    z2 = _karatsuba_recursive(a, c)
    z1 = _karatsuba_recursive(a + b, c + d) - z2 - z0

    return (z2 << (2 * m)) + (z1 << m) + z0


class KaratsubaCounter:
    def __init__(self):
        self.calls = 0

    def multiply(self, x: int, y: int) -> int:
        self.calls = 0
        return self._multiply(abs(x), abs(y))

    def _multiply(self, x: int, y: int) -> int:
        self.calls += 1

        if x < 16 or y < 16:
            return x * y

        n = max(x.bit_length(), y.bit_length())
        m = n // 2

        a = x >> m
        b = x & ((1 << m) - 1)

        c = y >> m
        d = y & ((1 << m) - 1)

        z0 = self._multiply(b, d)
        z2 = self._multiply(a, c)
        z1 = self._multiply(a + b, c + d) - z0 - z2

        return (z2 << (2 * m)) + (z1 << m) + z0


if __name__ == "__main__":
    a = 12345678901234567890
    b = 98765432109876543210

    print("Карацуба:", karatsuba(a, b))
    print("Python:  ", a * b)
    assert karatsuba(a, b) == a * b, "Результаты не совпадают!"
    print("Проверка пройдена успешно.")
