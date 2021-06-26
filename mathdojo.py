#!/usr/bin/env python

import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

    def value(self):
        return self.result


class MathDojoTest(unittest.TestCase):
    def test_adds(self):
        md = MathDojo()
        self.assertEqual(md.add(12).value(), 12)
        self.assertEqual(md.add(4, 3, 1).value(), 20)

    def test_subtracts(self):
        md = MathDojo()
        md.add(20)
        self.assertEqual(md.subtract(5).value(), 15)
        self.assertEqual(md.subtract(3, 2, 5).value(), 5)

    def test_chaining(self):
        md = MathDojo()
        self.assertEqual(md.add(12, 15).subtract(3, 5, 2).add(13).subtract(14).add(12).value(), 28)


if __name__ == '__main__':
    unittest.main()
