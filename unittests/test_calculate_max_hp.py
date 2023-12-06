from unittest import TestCase

from battle import calculate_max_hp


class TestCalculateMaxHp(TestCase):
    def test_smallest_level(self):
        pokemon_number = 4
        level = 1
        expected = 12
        self.assertEqual(expected, calculate_max_hp(pokemon_number, level))

    def test_not_smallest_level(self):
        pokemon_number = 4
        level = 5
        expected = 21
        self.assertEqual(expected, calculate_max_hp(pokemon_number, level))
