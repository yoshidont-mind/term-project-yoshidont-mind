from unittest import TestCase
from battle import attacks


class TestAttacks(TestCase):
    def test_damage_is_bigger_than_hp(self):
        offense = {'Name': 'Pikachu', 'Level': 10, 'Attack': 1}
        defense = {'Name': 'Mew', 'Defense': 1, 'HP': 5, 'Max HP': 10}
        attacks(offense, defense)
        actual = defense['HP']
        expected = 0
        self.assertEqual(actual, expected)

    def test_damage_and_hp_are_equal(self):
        offense = {'Name': 'Pikachu', 'Level': 10, 'Attack': 1}
        defense = {'Name': 'Mew', 'Defense': 1, 'HP': 7, 'Max HP': 10}
        attacks(offense, defense)
        actual = defense['HP']
        expected = 0
        self.assertEqual(actual, expected)

    def test_damage_is_smaller_than_hp(self):
        offense = {'Name': 'Pikachu', 'Level': 10, 'Attack': 1}
        defense = {'Name': 'Mew', 'Defense': 1, 'HP': 10, 'Max HP': 10}
        attacks(offense, defense)
        actual = defense['HP']
        expected = 3
        self.assertEqual(actual, expected)
