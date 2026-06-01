import unittest
import random

from karatsuba.karatsuba import karatsuba


class TestKaratsuba(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(
            karatsuba(0, 12345),
            0
        )

    def test_one(self):
        self.assertEqual(
            karatsuba(1, 99999),
            99999
        )

    def test_small(self):
        self.assertEqual(
            karatsuba(12, 34),
            408
        )

    def test_medium(self):
        self.assertEqual(
            karatsuba(123, 456),
            56088
        )

    def test_large(self):
        self.assertEqual(
            karatsuba(9999, 9999),
            9999 * 9999
        )

    def test_negative(self):
        self.assertEqual(
            karatsuba(-123, 456),
            -56088
        )

    def test_random(self):

        for _ in range(1000):

            a = random.randint(
                -10**8,
                10**8
            )

            b = random.randint(
                -10**8,
                10**8
            )

            self.assertEqual(
                karatsuba(a, b),
                a * b
            )


if __name__ == "__main__":
    unittest.main()
