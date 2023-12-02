from unittest import TestCase

from battle import next_pokemon


class TestNextPokemon(TestCase):
    def test_smallest_length(self):
        character = {'Pokemon': [{'Name': 'Charmander', 'HP': 1}]}
        actual = next_pokemon(character)
        expected = {'Name': 'Charmander', 'HP': 1}
        self.assertEqual(actual, expected)

    def test_middle_length_and_top_pokemon_alive(self):
        character = {'Pokemon': [{'Name': 'Eevee', 'HP': 1}, {'Name': 'Pikachu', 'HP': 0}, {'Name': 'Mew', 'HP': 1}]}
        actual = next_pokemon(character)
        expected = {'Name': 'Eevee', 'HP': 1}
        self.assertEqual(actual, expected)

    def test_middle_length_and_top_pokemon_dead(self):
        character = {'Pokemon': [{'Name': 'Eevee', 'HP': 0}, {'Name': 'Pikachu', 'HP': 0}, {'Name': 'Mew', 'HP': 1}]}
        actual = next_pokemon(character)
        expected = {'Name': 'Mew', 'HP': 1}
        self.assertEqual(actual, expected)

    def test_largest_length_and_top_pokemon_alive(self):
        character = {'Pokemon': [{'Name': 'Eevee', 'HP': 10}, {'Name': 'Pikachu', 'HP': 0}, {'Name': 'Mew', 'HP': 1},
                                 {'Name': 'Charmander', 'HP': 0}, {'Name': 'Bulbasaur', 'HP': 1},
                                 {'Name': 'Squirtle', 'HP': 0}]}
        actual = next_pokemon(character)
        expected = {'Name': 'Eevee', 'HP': 10}
        self.assertEqual(actual, expected)

    def test_large_length_and_top_pokemon_dead(self):
        character = {'Pokemon': [{'Name': 'Eevee', 'HP': 0}, {'Name': 'Pikachu', 'HP': 10}, {'Name': 'Mew', 'HP': 1},
                                 {'Name': 'Charmander', 'HP': 0}, {'Name': 'Bulbasaur', 'HP': 1},
                                 {'Name': 'Squirtle', 'HP': 0}]}
        actual = next_pokemon(character)
        expected = {'Name': 'Pikachu', 'HP': 10}
        self.assertEqual(actual, expected)
