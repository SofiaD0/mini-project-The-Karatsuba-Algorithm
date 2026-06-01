from karatsuba.karatsuba import KaratsubaCounter

counter = KaratsubaCounter()

a = 12345678
b = 87654321

result = counter.multiply(a, b)

print("Результат:", result)
print("Рекурсивные вызовы:", counter.calls)
