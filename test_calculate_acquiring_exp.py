from unittest import TestCase

from battle import calculate_acquiring_exp


class TestCalculateAcquiringExp(TestCase):
    def test_smallest_level(self):
        level = 1
        expected = 21
        actual = calculate_acquiring_exp(level)
        self.assertEqual(expected, actual)

    def test_not_smallest_level(self):
        level = 10
        expected = 214
        actual = calculate_acquiring_exp(level)
        self.assertEqual(expected, actual)
