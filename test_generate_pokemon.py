from unittest import TestCase

from battle import generate_pokemon


class TestGeneratePokemon(TestCase):
    def test_smallest_pokemon_number_and_smallest_level(self):
        actual = generate_pokemon(1, 1)
        expected = {'Attack': 6,
                    'Defense': 6,
                    'Exp': 0,
                    'Exp to next level': 1,
                    'HP': 12,
                    'Level': 1,
                    'Max HP': 12,
                    'Name': 'Bulbasaur',
                    'Number': 1}
        self.assertEqual(actual, expected)

    def test_smallest_pokemon_number_and_not_smallest_level(self):
        actual = generate_pokemon(1, 5)
        expected = {'Attack': 12,
                    'Defense': 12,
                    'Exp': 0,
                    'Exp to next level': 100,
                    'HP': 22,
                    'Level': 5,
                    'Max HP': 22,
                    'Name': 'Bulbasaur',
                    'Number': 1}
        self.assertEqual(actual, expected)

    def test_middle_pokemon_number_and_smallest_level(self):
        actual = generate_pokemon(8, 1)
        expected = {'Attack': 6,
                    'Defense': 6,
                    'Exp': 0,
                    'Exp to next level': 1,
                    'HP': 14,
                    'Level': 1,
                    'Max HP': 14,
                    'Name': 'Jigglypuff',
                    'Number': 8}
        self.assertEqual(actual, expected)

    def test_middle_pokemon_number_and_not_smallest_level(self):
        actual = generate_pokemon(8, 5)
        expected = {'Attack': 12,
                    'Defense': 9,
                    'Exp': 0,
                    'Exp to next level': 100,
                    'HP': 29,
                    'Level': 5,
                    'Max HP': 29,
                    'Name': 'Jigglypuff',
                    'Number': 8}
        self.assertEqual(actual, expected)

    def test_largest_pokemon_number_and_smallest_level(self):
        actual = generate_pokemon(17, 1)
        expected = {'Attack': 7,
                    'Defense': 7,
                    'Exp': 0,
                    'Exp to next level': 1,
                    'HP': 13,
                    'Level': 1,
                    'Max HP': 13,
                    'Name': 'Mew',
                    'Number': 17}
        self.assertEqual(actual, expected)

    def test_largest_pokemon_number_and_not_smallest_level(self):
        actual = generate_pokemon(17, 5)
        expected = {'Attack': 17,
                    'Defense': 17,
                    'Exp': 0,
                    'Exp to next level': 100,
                    'HP': 27,
                    'Level': 5,
                    'Max HP': 27,
                    'Name': 'Mew',
                    'Number': 17}
        self.assertEqual(actual, expected)
