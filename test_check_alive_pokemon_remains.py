from unittest import TestCase

from battle import check_alive_pokemon_remains


class TestCheckAlivePokemonRemains(TestCase):
    def test_smallest_length_and_alive_pokemon_remains(self):
        character = {'Pokemon': [{'HP': 1}]}
        actual = check_alive_pokemon_remains(character)
        expected = True
        self.assertEqual(actual, expected)

    def test_smallest_length_and_alive_pokemon_not_remains(self):
        character = {'Pokemon': [{'HP': 0}]}
        actual = check_alive_pokemon_remains(character)
        expected = False
        self.assertEqual(actual, expected)

    def test_middle_length_and_alive_pokemon_remains(self):
        character = {'Pokemon': [{'HP': 1}, {'HP': 0}, {'HP': 1}]}
        actual = check_alive_pokemon_remains(character)
        expected = True
        self.assertEqual(actual, expected)

    def test_middle_length_and_alive_pokemon_not_remains(self):
        character = {'Pokemon': [{'HP': 0}, {'HP': 0}, {'HP': 0}]}
        actual = check_alive_pokemon_remains(character)
        expected = False
        self.assertEqual(actual, expected)

    def test_largest_length_and_alive_pokemon_remains(self):
        character = {'Pokemon': [{'HP': 0}, {'HP': 0}, {'HP': 1}, {'HP': 0}, {'HP': 1}, {'HP': 0}]}
        actual = check_alive_pokemon_remains(character)
        expected = True
        self.assertEqual(actual, expected)

    def test_largest_length_and_alive_pokemon_not_remains(self):
        character = {'Pokemon': [{'HP': 0}, {'HP': 0}, {'HP': 0}, {'HP': 0}, {'HP': 0}, {'HP': 0}]}
        actual = check_alive_pokemon_remains(character)
        expected = False
        self.assertEqual(actual, expected)
