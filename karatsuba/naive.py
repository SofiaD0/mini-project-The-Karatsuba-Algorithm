def naive_multiply(a: int, b: int) -> int:
    result = 0

    shift = 0

    while b > 0:
        digit = b % 10

        result += a * digit * (10 ** shift)

        shift += 1
        b //= 10

    return result


if __name__ == "__main__":
    print(naive_multiply(123, 456))