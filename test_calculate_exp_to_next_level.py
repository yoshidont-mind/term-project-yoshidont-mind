from unittest import TestCase

from battle import calculate_exp_to_next_level


class TestCalculateExpToNextLevel(TestCase):
    def test_smallest_level(self):
        level = 1
        expected = 1
        actual = calculate_exp_to_next_level(level)
        self.assertEqual(expected, actual)

    def test_not_smallest_level(self):
        level = 10
        expected = 800
        actual = calculate_exp_to_next_level(level)
        self.assertEqual(expected, actual)
