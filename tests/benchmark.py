import random
import time

from karatsuba.karatsuba import karatsuba
from karatsuba.naive import naive_multiply


def generate_number(digits):
    first = str(random.randint(1, 9))
    rest = ''.join(
        str(random.randint(0, 9))
        for _ in range(digits - 1)
    )
    return int(first + rest)


sizes = [10, 50, 100, 500]

print(
    f"{'Digits':<10}"
    f"{'Naive (s)':<15}"
    f"{'Karatsuba (s)':<15}"
)

for digits in sizes:

    a = generate_number(digits)
    b = generate_number(digits)

    start = time.perf_counter()
    naive_multiply(a, b)
    naive_time = time.perf_counter() - start

    start = time.perf_counter()
    karatsuba(a, b)
    karatsuba_time = time.perf_counter() - start

    print(
        f"{digits:<10}"
        f"{naive_time:<15.6f}"
        f"{karatsuba_time:<15.6f}"
    )