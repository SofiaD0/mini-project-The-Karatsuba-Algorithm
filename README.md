# Karatsuba Multiplication Algorithm

Mini-project for the Algorithms and Data Structures course.

## Project Overview

This project implements the Karatsuba multiplication algorithm for large integers and compares its behavior with a naive multiplication approach.

Karatsuba's algorithm is a divide-and-conquer method that reduces the number of recursive multiplications from four to three, improving the asymptotic complexity from:

* Naive multiplication: O(n²)
* Karatsuba multiplication: O(n^1.585)

where:

log₂(3) ≈ 1.585

---

## Project Structure

```text
mini-project-The-Karatsuba-Algorithm/

├── karatsuba/
│   ├── __init__.py
│   ├── karatsuba.py
│   └── naive.py
│
├── tests/
│   ├── test_karatsuba.py
│   ├── benchmark.py
│   └── recursion_demo.py
│
└── README.md
```

---

## Implemented Components

### Karatsuba Algorithm

File:

```text
karatsuba/karatsuba.py
```

Features:

* Recursive divide-and-conquer multiplication
* Three recursive multiplications instead of four
* Support for arbitrarily large integers
* Recursive call counter for demonstration purposes

---

### Naive Multiplication

File:

```text
karatsuba/naive.py
```

Features:

* Classical schoolbook multiplication approach
* Used as a baseline for comparison

---

## Testing

Unit tests are located in:

```text
tests/test_karatsuba.py
```

Test cases include:

* Multiplication by zero
* Multiplication by one
* Small predefined examples
* Large predefined examples
* Randomized testing against Python's built-in multiplication

Run tests:

```bash
python -m unittest tests.test_karatsuba
```

Expected output:

```text
......
----------------------------------------------------------------------
Ran 6 tests

OK
```

---

## Performance Benchmark

Benchmark script:

```text
tests/benchmark.py
```

Run:

```bash
python -m tests.benchmark
```

Example output:

```text
Digits    Naive (s)      Karatsuba (s)

100       0.000141       0.001312
500       0.001959       0.014086
1000      0.012037       0.042549
2000      0.073312       0.243758
```

---

## Recursive Call Demonstration

Demonstration script:

```text
tests/recursion_demo.py
```

Run:

```bash
python -m tests.recursion_demo
```

Example output:

```text
Result: 1082152022374638
Recursive calls: 49
```

This demonstrates the recursive nature of the Karatsuba algorithm and the reduction in multiplication operations compared to the classical divide-and-conquer approach.

---

## Conclusion

The project successfully implements the Karatsuba multiplication algorithm and verifies its correctness through automated testing.

Although Python's built-in multiplication remains faster due to low-level optimizations, the implementation demonstrates the theoretical improvement of Karatsuba's method and its divide-and-conquer strategy.
