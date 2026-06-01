from karatsuba.karatsuba import KaratsubaCounter

counter = KaratsubaCounter()

a = 12345678
b = 87654321

result = counter.multiply(a, b)

print("Result:", result)
print("Recursive calls:", counter.calls)
