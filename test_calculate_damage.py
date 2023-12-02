from unittest import TestCase

from battle import calculate_damage


class TestCalculateDamage(TestCase):
    def test_smallest_level_smallest_attack_and_smallest_defense(self):
        offense = {'Level': 1, 'Attack': 1}
        defense = {'Defense': 1}
        actual = calculate_damage(offense, defense)
        expected = 4
        self.assertEqual(actual, expected)

    def test_smallest_level_smallest_attack_and_not_smallest_defense(self):
        offense = {'Level': 1, 'Attack': 1}
        defense = {'Defense': 10}
        actual = calculate_damage(offense, defense)
        expected = 2
        self.assertEqual(actual, expected)

    def test_smallest_level_not_smallest_attack_and_smallest_defense(self):
        offense = {'Level': 1, 'Attack': 10}
        defense = {'Defense': 1}
        actual = calculate_damage(offense, defense)
        expected = 21
        self.assertEqual(actual, expected)

    def test_smallest_level_not_smallest_attack_and_not_smallest_defense(self):
        offense = {'Level': 1, 'Attack': 10}
        defense = {'Defense': 10}
        actual = calculate_damage(offense, defense)
        expected = 4
        self.assertEqual(actual, expected)

    def test_not_smallest_level_smallest_attack_and_smallest_defense(self):
        offense = {'Level': 10, 'Attack': 1}
        defense = {'Defense': 1}
        actual = calculate_damage(offense, defense)
        expected = 7
        self.assertEqual(actual, expected)

    def test_not_smallest_level_smallest_attack_and_not_smallest_defense(self):
        offense = {'Level': 10, 'Attack': 1}
        defense = {'Defense': 10}
        actual = calculate_damage(offense, defense)
        expected = 2
        self.assertEqual(actual, expected)

    def test_not_smallest_level_not_smallest_attack_and_smallest_defense(self):
        offense = {'Level': 10, 'Attack': 10}
        defense = {'Defense': 1}
        actual = calculate_damage(offense, defense)
        expected = 50
        self.assertEqual(actual, expected)

    def test_not_smallest_level_not_smallest_attack_and_not_smallest_defense(self):
        offense = {'Level': 10, 'Attack': 10}
        defense = {'Defense': 10}
        actual = calculate_damage(offense, defense)
        expected = 7
        self.assertEqual(actual, expected)
