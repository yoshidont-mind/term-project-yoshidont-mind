from unittest import TestCase

from battle import append_pokemon


class TestAppendPokemon(TestCase):
    def test_smallest_level_and_smallest_hp(self):
        character = {'Name': 'Ash', 'Pokemon': []}
        pokemon_number = 1
        level = 1
        pokemon_hp = 1
        append_pokemon(character, pokemon_number, level, pokemon_hp)
        actual = {'Name': character['Pokemon'][0]['Name'], 'Level': character['Pokemon'][0]['Level'],
                  'HP': character['Pokemon'][0]['HP']}
        expected = {'Name': 'Bulbasaur', 'Level': 1, 'HP': 1}
        self.assertEqual(actual, expected)

    def test_smallest_level_and_not_smallest_hp(self):
        character = {'Name': 'Ash', 'Pokemon': []}
        pokemon_number = 1
        level = 1
        pokemon_hp = 10
        append_pokemon(character, pokemon_number, level, pokemon_hp)
        actual = {'Name': character['Pokemon'][0]['Name'], 'Level': character['Pokemon'][0]['Level'],
                  'HP': character['Pokemon'][0]['HP']}
        expected = {'Name': 'Bulbasaur', 'Level': 1, 'HP': 10}
        self.assertEqual(actual, expected)

    def test_not_smallest_level_and_smallest_hp(self):
        character = {'Name': 'Ash', 'Pokemon': []}
        pokemon_number = 1
        level = 5
        pokemon_hp = 1
        append_pokemon(character, pokemon_number, level, pokemon_hp)
        actual = {'Name': character['Pokemon'][0]['Name'], 'Level': character['Pokemon'][0]['Level'],
                  'HP': character['Pokemon'][0]['HP']}
        expected = {'Name': 'Bulbasaur', 'Level': 5, 'HP': 1}
        self.assertEqual(actual, expected)

    def test_not_smallest_level_and_not_smallest_hp(self):
        character = {'Name': 'Ash', 'Pokemon': []}
        pokemon_number = 1
        level = 5
        pokemon_hp = 10
        append_pokemon(character, pokemon_number, level, pokemon_hp)
        actual = {'Name': character['Pokemon'][0]['Name'], 'Level': character['Pokemon'][0]['Level'],
                  'HP': character['Pokemon'][0]['HP']}
        expected = {'Name': 'Bulbasaur', 'Level': 5, 'HP': 10}
        self.assertEqual(actual, expected)
