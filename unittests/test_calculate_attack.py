from unittest import TestCase

from battle import calculate_attack


class TestCalculateAttack(TestCase):
    def test_smallest_level(self):
        pokemon_number = 8
        level = 1
        expected = 6
        actual = calculate_attack(pokemon_number, level)
        self.assertEqual(expected, actual)

    def test_not_smallest_level(self):
        pokemon_number = 8
        level = 10
        expected = 19
        actual = calculate_attack(pokemon_number, level)
        self.assertEqual(expected, actual)
