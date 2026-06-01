import random
import time
import sys
from pathlib import Path

sys.set_int_max_str_digits(100000)

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from karatsuba.karatsuba import karatsuba
from karatsuba.naive import naive_multiply


def generate_number(digits):
    first = str(random.randint(1, 9))
    rest = ''.join(
        str(random.randint(0, 9))
        for _ in range(digits - 1)
    )
    return int(first + rest)


sizes = [100, 500, 1000, 2000, 5000, 10000]

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
