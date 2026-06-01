from karatsuba.karatsuba import KaratsubaCounter

sizes = [(1234, 5678), (12345678, 87654321), (1234567890123456, 9876543210987654)]

for a, b in sizes:

    counter = KaratsubaCounter()

    counter.multiply(a, b)

    print(f"цифры = {len(str(a))}, количества рекурсивных вызовов = {counter.calls}")
