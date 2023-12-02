from unittest import TestCase

from battle import calculate_defense


class TestCalculateDefense(TestCase):
    def test_smallest_level(self):
        pokemon_number = 8
        level = 1
        expected = 6
        actual = calculate_defense(pokemon_number, level)
        self.assertEqual(expected, actual)

    def test_not_smallest_level(self):
        pokemon_number = 8
        level = 10
        expected = 14
        actual = calculate_defense(pokemon_number, level)
        self.assertEqual(expected, actual)
